from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, forms
from django.views.decorators.csrf import csrf_exempt

from .forms import PatientForm, ReviewForm
from django.contrib import messages

from .models import Review

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():

            patient = form.save(commit=False)
            patient.save()

            messages.success(request, 'Registration successful! Your patient record has been created.')

            return redirect('login')

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
        # Calculăm numărul de stele pline și goale
        full_stars = int(review.average_rating)  # Stele pline
        empty_stars = 5 - full_stars  # Stele goale

        # Adăugăm listele de stele pline și goale
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

def request_offer(request):
    return render(request, 'request-offer.html')

def feedback_survey(request):
    categories = ['patient', 'doctor', 'partner', 'patient_rep']
    rating_range = range(1,6)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully submitted your review!')
            return redirect('community')  # Redirect to the community page to display the review
    else:
        form = ReviewForm()
    return render(request, 'feedback-survey.html', {'form': form})