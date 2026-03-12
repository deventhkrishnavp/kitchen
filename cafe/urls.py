from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('reviews/', views.reviews, name='reviews'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
]
