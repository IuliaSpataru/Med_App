from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    CATEGORY_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('partner', 'Partner'),
        ('patient_representative', 'Patient Representative'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    rating_1 = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    rating_2 = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    rating_3 = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    rating_4 = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    rating_5 = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    @property
    def average_rating(self):
        return (self.rating_1 + self.rating_2 + self.rating_3 + self.rating_4 + self.rating_5) / 5

    def __str__(self):
        return f"{self.name} - {self.category} - {self.date_posted}"





