from django.urls import path
from . import views

urlpatterns = [
    path('date', views.date),
    path('horoscope/<slug:name_zodiac>', views.info, name='zodiac'),
    path('', views.main),
    path('profile', views.profile_view, name='profile')
]