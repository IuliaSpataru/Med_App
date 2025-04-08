from random import choices

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from synccare.patients.models import Patient
from synccare.website.models import Review


# region 1. Registration Form

class PatientForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    accept_terms = forms.BooleanField(required=True, label="I hereby agree to the terms and conditions.")
    third_party = forms.BooleanField(required=True,
                                     label="I authorize the sharing of my information with a third party designated by me.")
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Date of Birth"
    )

    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'birth_date', 'gender', 'contact_number',
            'email_address', 'rep_first_name', 'rep_last_name', 'rep_contact_number',
            'room_number', 'ward', 'accept_terms', 'third_party'
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        patient = super().save(commit=False)

        # Create User object
        user = User.objects.create_user(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email_address'],
            username=self.cleaned_data['email_address'],  # email as username
            password=self.cleaned_data['password1'],

        )

        # link  patient to the new user
        patient.user = user

        if commit:
            user.save()
            patient.save()

        return patient

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







