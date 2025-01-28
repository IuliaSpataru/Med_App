from django.contrib import admin

from synccare.wards.models import Ward


# Register your models here.
@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('ward_name', 'head_of_department')
    search_fields = ('ward_name',)
    list_filter = ('ward_name',)