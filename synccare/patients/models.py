from django.db import models

# Create your models here.

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=15, null=True, blank=True)
    room_number = models.IntegerField(null=True, blank=True)
    admission_date = models.DateTimeField(auto_now_add=True)
    ward_choices = [
        ('Cardiology', 'Cardiology'),
        ('Rheumatology', 'Rheumatology'),
        ('Paediatrics', 'Paediatrics'),
        ('Oncology', 'Oncology'),
        ('Gastroenterology', 'Gastroenterology'),
        ('Physiotherapy', 'Physiotherapy'),
        ('Radiology', 'Radiology'),
    ]
    ward = models.CharField(max_length=50, choices=ward_choices)

    def __str__(self):
        return (f" Patient: {self.full_name} {self.last_name}, Gender: {self.gender}, born on {self.date_of_birth}, "
                f"Ward: {self.ward}, Admitted: {self.admission_date}")

