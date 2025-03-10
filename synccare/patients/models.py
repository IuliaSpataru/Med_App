from django.db import models
from django.utils.text import slugify

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True, default="")
    username=models.CharField(max_length=150, blank=True, null=True, default="")
    birth_date = models.DateField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    rep_first_name = models.CharField(max_length=100, null=True, blank=True)
    rep_last_name = models.CharField(max_length=100, null=True, blank=True)
    rep_contact_number = models.CharField(max_length=15, null=True, blank=True)
    room_number = models.IntegerField(null=True, blank=True)
    admission_date = models.DateTimeField(auto_now_add=True)
    WARD_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Rheumatology', 'Rheumatology'),
        ('Paediatrics', 'Paediatrics'),
        ('Oncology', 'Oncology'),
        ('Gastroenterology', 'Gastroenterology'),
        ('Physiotherapy', 'Physiotherapy'),
        ('Radiology', 'Radiology'),
    ]
    ward = models.CharField(max_length=50, choices=WARD_CHOICES)

    def save(self, *args, **kwargs):
        if not self.username:
            base_username = slugify(f"{self.first_name}{self.last_name}")[:30]
            username = base_username
            counter = 1
            while Patient.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            self.username = username
        super().save(*args, **kwargs)

    def __str__(self):
        return (f" Patient: {self.full_name} {self.last_name}, Gender: {self.gender}, born on {self.date_of_birth}, "
                f"Ward: {self.ward}, Admitted: {self.admission_date}")

