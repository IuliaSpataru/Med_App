from django.contrib import admin
from synccare.patients.models import Patient


# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'gender', 'room_number', 'admission_date', 'ward')
    list_filter = ('ward', 'gender')
    search_fields = ('full_name', 'room_number')
