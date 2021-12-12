from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('faq/', views.faq, name='faq'),
    path('contacts/', views.contacts, name='contacts'),
    path('rates/', views.rates, name='rates'),
    path('gallery/', views.reviews, name='gallery'),
    path('getimages/', views.getimages, name='getimages'),

]