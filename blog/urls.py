from blog.views import *
from django.urls import path
urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('service', service, name="service"),
    path('menu/', menu, name="menu"),
    path('team/', team, name="team"),
    path('testimonial', testimonial, name="testimonial"),
    path('detel/<slug:slug>/', index_detel, name="detel"),
    path('home-create',Home5CreateView.as_view(), name="home-create"),
    path('home-update/<int:pk>/',Home5UpdateView.as_view(), name="home-update"),
    path('home-delete/<int:pk>/',Home5DeleteView.as_view(), name="home-delete"),

     ]