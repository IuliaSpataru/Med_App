from django.shortcuts import render, redirect


# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html', {'user': request.user})


def doctors(request):
    return render(request, 'doctors.html')


def specialties(request):
    return render(request, 'specialties.html')


def centers(request):
    return render(request, 'centers.html')


def prices(request):
    return render(request, 'prices.html')


def patients(request):
    return render(request, 'patients.html')


def about_us(request):
    return render(request, 'about_us.html')


def contact_us(request):
    return render(request, 'contact_us.html')
