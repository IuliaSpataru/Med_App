# Generated by Django 4.2 on 2025-01-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_staff_ward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(choices=[('Nurse', 'Nurse'), ('Assistant', 'Assistant'), ('Attending Doctor', 'Attending Doctor'), ('Head of Department', 'Head of Department'), ('Hospital Manager', 'Hospital Manager')], max_length=100),
        ),
    ]
