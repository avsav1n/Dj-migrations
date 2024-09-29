from django.contrib import admin

from .models import Student, Teacher


class StydingInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 0

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    inlines = [StydingInline]
    exclude = ['teachers']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    inlines = [StydingInline]
