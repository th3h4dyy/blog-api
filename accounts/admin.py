from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ("email", "username", "name", "is_staff")
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
