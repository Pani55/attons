from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """  Admin interface for accessing users. """

    list_display = ("id", "email", "phone", "city", "is_staff", "is_superuser", "is_active",)
