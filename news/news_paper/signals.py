from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post


@receiver(post_save, sender=Post)
def Post_created(instance, created, **kwargs):
    if not created:
        return
    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject= f'Новый пост в категории {instance.category}'

    text_content = (
        f'Публикация: {instance.title}\n'
        f'Категории: {instance.category}'
        f'Ссылка на публикацию: http://127.0.0.1{instance.get_absolute_url()}'
    )

    html_content = (
        f'Заголовок: {instance.title}<br>'
        f'Категории: {instance.category}<br>'
        f'<a href = "http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на публикацию</a>'
    )

    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
