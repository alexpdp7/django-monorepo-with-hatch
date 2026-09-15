from django.core.management.base import BaseCommand, CommandError
import plain


class Command(BaseCommand):
    help = "Sample command that uses a non-Django workspace member"

    def handle(self, *args, **options):
        print(plain.foo())
