from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional information", {"fields": ("address",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional information", {"fields": ("email", "address")}),
    )
    list_display = ("email", "username", "is_staff", "is_active")
    search_fields = ("email", "username")
