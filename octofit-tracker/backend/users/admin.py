from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'grade_level', 'fitness_level', 'total_points', 'is_active')
    list_filter = ('grade_level', 'fitness_level', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

    fieldsets = UserAdmin.fieldsets + (
        ('Fitness Profile', {
            'fields': ('grade_level', 'fitness_level', 'total_points', 'profile_picture')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Fitness Profile', {
            'fields': ('first_name', 'last_name', 'grade_level', 'fitness_level', 'profile_picture')
        }),
    )
