from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, forms
from django.views.decorators.csrf import csrf_exempt

import synccare
from .forms import PatientForm, ReviewForm
from django.contrib import messages
from django.core.mail import send_mail

from .models import Review

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Your patient record has been created.')
            return redirect('login')
        else:
            print(form.errors)
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        form = PatientForm()

    return render(request, 'register.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

def home(request):
    return render(request, 'home.html', {'user': request.user})

def community(request):
    reviews = Review.objects.all().order_by('-date_posted')

    for review in reviews:
        full_stars = int(review.average_rating)
        empty_stars = 5 - full_stars
        review.full_stars = ['⭐'] * full_stars
        review.empty_stars = ['☆'] * empty_stars

    return render(request, 'community.html', {'reviews': reviews})

def centers(request):
    return render(request, 'centers.html')

def prices(request):
    return render(request, 'prices.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def patient_portal(request):
    return render(request, 'patient-portal.html')

def feedback_survey(request):
    categories = ['patient', 'doctor', 'partner', 'patient_rep']
    rating_range = range(1,6)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully submitted your review!')
            return redirect('community')
    else:
        form = ReviewForm()
    return render(request, 'feedback-survey.html', {'form': form})


def request_offer(request):
    if request.method == 'POST':
        center_name = request.POST['center_name']
        center_type = request.POST['center_type']
        center_country = request.POST['center_country']
        center_city = request.POST['center_city']
        center_capacity = request.POST['center_capacity']
        contact_person = request.POST['contact_person']
        email = request.POST['email']
        phone = request.POST['phone']
        additional_info = request.POST['additional_info']

        send_mail(
            subject=f'New Offer Request from {center_name}',
            message=f"""
            Center Name: {center_name}
            Center Type: {center_type}
            Center Country: {center_country}
            Center City: {center_city}
            Center Capacity: {center_capacity}
            Contact Person: {contact_person}
            Email: {email}
            Phone: {phone}
            Additional Info: {additional_info}
            """,
            from_email='no-reply@synccare.com',
            recipient_list=[],
            fail_silently=False,
        )

        messages.success(request, 'You have successfully sent your request. '
                                  'You will be contacted within the next 24 hrs with a personalized offer. '
                                  'Thank you for your interest in SynCCare! ')
        return render(request, 'request-offer.html')

    return render(request, 'request-offer.html')