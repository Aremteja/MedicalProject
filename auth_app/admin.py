from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'name', 'height', 'weight', 'gender', 'is_staff', 'is_admin', 'is_active']


admin.site.register(User, UserAdmin)
