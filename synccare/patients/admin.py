from django.contrib import admin
from synccare.patients.models import Patient


# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'gender', 'room_number', 'admission_date', 'ward')
    list_filter = ('ward', 'gender')
    search_fields = ('first_name', 'last_name', 'room_number')
