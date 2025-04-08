from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register_patient/', views.register_patient, name='register'),
    path('home/', views.home, name='home'),
    path('community/', views.community, name='community'),
    path('centers/', views.centers, name='centers'),
    path('prices/', views.prices, name='prices'),
    path('about_us/', views.about_us, name='about_us'),
    path('feedback-survey/', views.feedback_survey, name='feedback-survey'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('patient_portal/', views.patient_portal, name='patient-portal'),
    path('request_offer/', views.request_offer, name='request-offer'),


]
