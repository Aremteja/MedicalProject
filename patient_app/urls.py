from django.urls import path
from . import views


app_name = 'patient_app'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('patient/patient-data-entry/', views.patient_data_enter_view, name='data_entry'),
    path('patient/dashboard/', views.patient_dashboard, name='dashboard'),
]
