from django.db import models

# Create your models here.

class Task(models.Model):
    task_description = models.TextField()
    assigned_to = models.ForeignKey('staff.Staff', on_delete=models.SET_NULL, null=True, blank=True)
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    deadline = models.DateTimeField()
    status_choices = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')

    def __str__(self):
        return f"Task: {self.task_description} for {self.patient.first_name}{self.patient.last_name} - Status: {self.status}"