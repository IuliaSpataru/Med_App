from random import choices

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from synccare.patients.models import Patient


class PatientForm(forms.ModelForm):


    first_name = forms.CharField(max_length=100, label="First Name", required=True)
    last_name = forms.CharField(max_length=100, label="Last Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), label="Date of Birth", required=True)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender", required=True)
    contact_number = forms.CharField(max_length=15, label="Contact Number", required=True)
    email_address = forms.EmailField(label="Email Address", required=True)

    rep_first_name = forms.CharField(max_length=100, label="Third Party First Name", required=True)
    rep_last_name = forms.CharField(max_length=100, label="Third Party Last Name", required=True)
    rep_contact_number = forms.CharField(max_length=15, label="Third Party Contact Number", required=True)


    room_number = forms.IntegerField(label="Room Number", required=False)
    WARD_CHOICES = [
        ('---', '---'),
        ('Cardiology', 'Cardiology'),
        ('Rheumatology', 'Rheumatology'),
        ('Paediatrics', 'Paediatrics'),
        ('Oncology', 'Oncology'),
        ('Gastroenterology', 'Gastroenterology'),
        ('Physiotherapy', 'Physiotherapy'),
        ('Radiology', 'Radiology'),
    ]
    ward = forms.ChoiceField(choices=WARD_CHOICES, label="Assigned Ward", required=True)


    password1 = forms.CharField(widget=forms.PasswordInput, label="Create password", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password", required=True)
    accept_terms = forms.BooleanField(label="I accept the Terms & Conditions", required=True)
    third_party = forms.BooleanField(label="I hereby give my consent for my health aide to be granted access to this account.", required=True)

    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'birth_date', 'gender', 'contact_number', 'email_address',
            'rep_first_name', 'rep_last_name', 'rep_contact_number', 'room_number', 'ward',
            'password1', 'password2', 'accept_terms', 'third_party'
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2
