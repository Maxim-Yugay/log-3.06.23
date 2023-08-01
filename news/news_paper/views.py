import pytz
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django_filters import FilterSet, DateFilter
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.cache import cache
from django.utils import timezone
from django.utils.translation import activate, get_supported_language_variant
from django.utils.translation import gettext as _
from rest_framework import serializers

from .models import *
from .filters import PostFilter
from .forms import PostForm

import logging

logger = logging.getLogger(__name__)



class AuthorList(ListView):
    model = Author
    context_object_name = 'Author'

class PostList(ListView):
    model = Post
    context_object_name = 'post'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}')

        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
            return obj


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news_paper.add_post')
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'news_paper/post_edit.html'


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news_paper.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news_paper/post_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news_paper.delete_post')
    model = Post
    template_name = 'news_paper/post_delete.html'
    success_url = reverse_lazy('news')


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, category=category)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                category=category,
            ).delete()
    categories_with_subscriptions = Category.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
                category=OuterRef('pk'),
            )
        )
    ).order_by('name')
    return render(
        request,
        'news_paper/subscriptions.html',
        {'categories': categories_with_subscriptions},
    )

