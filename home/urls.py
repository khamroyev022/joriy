from django.urls import path
from .views import about, home, testimonial, contact, about, cources, team, error
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('cources/', cources, name='cources'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('error/', error, name='error'),
]
