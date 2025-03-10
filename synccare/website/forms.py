from random import choices

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from synccare.patients.models import Patient
from synccare.website.models import Review


# region 1. Registration Form

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
        exclude = ['username']
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

#endregion

#region 2. Review Form

class ReviewForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('---', '---'),
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('partner', 'Partner'),
        ('patient_rep', 'Patient Representative'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True)
    name = forms.CharField(max_length=100, label="Name", required=True)


    class Meta:
        model = Review
        fields = ['name', 'category', 'rating_1', 'rating_2', 'rating_3', 'rating_4', 'rating_5', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        category_questions = {
            'patient': [
                'How would you rate the ease of use of the SynCCare app?',
                'Did you find the treatment information clear and accessible?',
                'How would you rate your interactions with medical staff through the app?',
                'Did the app help you understand your treatment progress better?',
                'Would you recommend the SynCCare app to other patients?'
            ],
            'doctor': [
                'How would you rate the effectiveness of the SynCCare app in managing patients?',
                'Does the app provide the necessary information for you to make quick decisions?',
                'How well does the app support collaboration with other doctors and medical staff?',
                'Does the app facilitate clear and fast communication with patients?',
                'Would you recommend the SynCCare app to other doctors?'
            ],
            'partner': [
                'How would you rate your collaboration with the SynCCare app within your partnership?',
                'Does the app facilitate information exchange between parties?',
                'How well does the app address the needs of your organization?',
                'How would you rate the impact of the app on collaboration between teams?',
                'Would you recommend the SynCCare app to other partners?'
            ],
            'patient_rep': [
                'How would you rate how well the SynCCare app helps manage patient cases?',
                'Does the app provide enough information to support patients and their families?',
                'How does the app support communication with the medical staff of patients?',
                'Did you find the app useful in tracking the patient’s health status?',
                'Would you recommend the SynCCare app to other patient representatives?'
            ]
        }

        if 'category' in self.data:
            category = self.data.get('category')
            if category in category_questions:
                for i, question in enumerate(category_questions[category], start=1):
                    self.fields[f'rating_{i}'].label = question

#endregion







