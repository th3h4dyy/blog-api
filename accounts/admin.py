from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ("email", "username", "name", "is_staff")
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
