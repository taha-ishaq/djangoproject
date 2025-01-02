from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # About Us page
    path('contact/', views.contact, name='contact'),  # Contact Us page 
]
