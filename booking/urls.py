from django.contrib import admin
from django.urls import path
from booking import views

urlpatterns = [
    path('', views.main_page, name="main"),
    path('rooms/<int:room_id>', views.booking_page, name='booking_system')
] 