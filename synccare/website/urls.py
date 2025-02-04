from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('doctors/', views.doctors, name='doctors'),
    path('specialties/', views.specialties, name='specialties'),
    path('centers/', views.centers, name='centers'),
    path('prices/', views.prices, name='prices'),
    path('patients/', views.patients, name='patients'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
