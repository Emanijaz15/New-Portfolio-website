from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('certificates/', views.certificates, name='certificates'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
]