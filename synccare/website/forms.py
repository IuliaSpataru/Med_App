from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=100, label="First Name", required=True)
    last_name = forms.CharField(max_length=100, label="Last Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), label="Date of Birth", required=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender", required=True)
    contact_number = forms.CharField(max_length=100, label="Phone Number", required=True)

    third_party_first_name = forms.CharField(max_length=100, label="First Name", required=True)
    third_party_last_name = forms.CharField(max_length=100, label="Last Name", required=True)
    third_party_contact_number = forms.CharField(max_length=100, label="3rd Party Phone Number", required=True)

    password1 = forms.CharField(widget=forms.PasswordInput, label="Create password", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password", required=True)

    accept_terms = forms.BooleanField(label="I accept the Terms & Conditions", required=True)
    third_party = forms.BooleanField(
        label="I hereby give my consent for my health aide to be granted access to this account.",
        required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'gender', 'contact_number',
                  'third_party_first_name', 'third_party_last_name', 'third_party_contact_number',
                  'password1', 'password2', 'accept_terms', 'third_party']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

