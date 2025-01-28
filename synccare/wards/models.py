from django.db import models
from synccare.staff.models import Staff

# Create your models here.

class Ward(models.Model):
    ward_name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    head_of_department = models.ForeignKey(Staff,
                                           on_delete=models.SET_NULL,
                                           null=True,
                                           blank=True,
                                           related_name='wards')

    def __str__(self):
            return self.ward_name