from django.core.management.base import BaseCommand, CommandError
from news_paper.models import Post


class Command(BaseCommand):
    help = "Delete old posts"
    missing_args_message = 'Not enough arguments'
    requires_migrations_chek = True

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Do you really want to delete all posts? yes/no!')
        answer = input()

        if answer == 'yes':
            Post.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Succesfully wiped products!'))
            return

        self.stdout.write(self.style.ERROR('Access denied'))



