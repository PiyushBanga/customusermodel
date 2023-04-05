from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Student, Teacher, Class


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'is_active', 'is_staff', 'is_student', 'is_teacher')
    list_filter = ('is_active', 'is_staff', 'is_student', 'is_teacher')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_student', 'is_teacher')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_student', 'is_teacher')
        }),
    )
    search_fields = ('email', 'full_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
