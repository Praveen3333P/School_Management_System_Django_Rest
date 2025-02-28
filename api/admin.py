from django.contrib import admin
from .models import Student, Teacher, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'grade')
    search_fields = ('name', 'grade')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject')
    search_fields = ('name', 'subject')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'teacher')
    search_fields = ('title',)
