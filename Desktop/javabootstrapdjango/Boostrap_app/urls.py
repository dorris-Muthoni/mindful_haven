from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='my_index'),
    path('contact/', views.contact, name='my_contact'),
    path('therapist/', views.therapist, name='my_therapist'),
    path('about/', views.about, name='my_about'),

    path('service/',views.service,name='my_service')
]
