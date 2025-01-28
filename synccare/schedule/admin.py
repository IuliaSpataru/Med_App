from django.contrib import admin

from synccare.schedule.models import Schedule


# Register your models here.

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'shift', 'ward')
    list_filter = ('shift', 'ward')
    search_fields = ('name',)
    list_per_page = 10

