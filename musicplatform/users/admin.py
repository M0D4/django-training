from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserForm


class UserAdmin(BaseUserAdmin):
    form = UserForm
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Personal info', {'fields': ('bio',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Personal info', {'fields': ('bio',)}),
    )


admin.site.register(User, UserAdmin)
