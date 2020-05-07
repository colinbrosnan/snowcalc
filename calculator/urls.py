from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy')
]
