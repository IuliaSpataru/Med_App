from django.contrib import admin

from synccare.staff.models import Staff


# Register your models here.

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'ward')
    list_filter = ('role',)
    search_fields = ('name',)