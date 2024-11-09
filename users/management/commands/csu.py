from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """ Command to create a new superuser from command line """

    def handle(self, *args, **options):
        user = User.objects.create(email="admin@example.com")
        user.set_password("123666")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
