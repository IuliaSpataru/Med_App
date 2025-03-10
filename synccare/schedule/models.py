from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

# Create your models here.

class Schedule(models.Model):
    class Meta:
        verbose_name_plural = "Schedules"

    SHIFT_CHOICES = [
        ('Morning Shift', 'Morning - 07:00 - 16:00'),
        ('Middle Shift', 'Middle - 10:00 - 19:00'),
        ('Evening Shift', 'Evening - 15:00 - 00:00'),
        ('Night Shift', 'Night - 23:00 - 08:00'),
        ('OnCall Shift', 'OnCall - 00:00 - 00:00')
    ]

    name = models.ForeignKey('staff.Staff', on_delete=models.CASCADE)
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    ward = models.ForeignKey('wards.Ward', on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f' {self.name} - {self.shift}'

    @property
    def is_current_month(self):
        current_month = timezone.now().month
        return self.start_date.month == current_month

    @property
    def month(self):
        return self.start_date.strftime('%B %Y')


    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("End date cannot be earlier than start date.")