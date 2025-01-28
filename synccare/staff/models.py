from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Staff(models.Model):
    class Meta:
        verbose_name_plural = "Staff Members"

    ROLE_CHOICES = [
        ('Nurse', 'Nurse'),
        ('Assistant', 'Assistant'),
        ('Attending Doctor', 'Attending Doctor'),
        ('Head of Department', 'Head of Department'),
        ('Hospital Manager', 'Hospital Manager'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    ward = models.ForeignKey('wards.Ward', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f" Name: {self.name}, Role: {self.role}"

