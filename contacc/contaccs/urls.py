from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactList, name='home'),
    path('form/', views.contactCreate),
    path('create/', views.contactCreatePOST),
    path('read/<str:contact_id>/', views.contactRead),
    path('updateform/<str:contact_id>/', views.contactUpdate),
    path('update/<str:contact_id>/', views.contactUpdatePOST),
    path('delete/<str:contact_id>/', views.contactDelete, name='delete_view'),
    path('deleteconfirm/<str:contact_id>/', views.contactDeleteConfirm)
    #path('filter/', views.contactFilterPOST),
    #path('filterresults/', views.contactFilter)
]
