from django.contrib import admin
# from django.contrib.gis.gdal import field
from modeltranslation.admin import TranslationAdmin

from .models import *


def nullfy_rating(modeladmin, rating, queryset):
    queryset.update(rating=0)
nullfy_rating.short_description = 'Nullfy rating'

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'dateCreation', 'categoryType', 'rating',)
    list_filter = ('dateCreation', 'categoryType')
    search_fields = ('dateCreation', 'categoryType')
    actions = [nullfy_rating]

