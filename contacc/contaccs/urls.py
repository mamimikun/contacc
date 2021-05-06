from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactList),
    path('create/', views.contactCreate),
    path('read/<str:contact_id>/', views.contactRead),
    path('update/<str:contact_id>/', views.contactUpdate),
    path('delete/<str:contact_id>/', views.contactDelete)
]
