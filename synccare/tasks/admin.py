from django.contrib import admin

from synccare.tasks.models import Task


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('assigned_to', 'deadline', 'status')
    list_filter = ('status',)
    search_fields = ('assigned_to', 'deadline')