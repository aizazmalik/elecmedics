from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctors/', views.doctors, name='doctors'),
    path('newpatient/', views.newpatient, name='newpatient'),
    path('existingpatient/', views.existingpatient, name='existingpatient'),
    path('addnewpatient/', views.addnewpatient, name='addnewpatient'),
    path('addnewprescription/', views.addnewprescription, name='addnewprescription'),
    


]