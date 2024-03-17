from django.contrib import admin
from .models import PatientHealthModel


class PatientHealthModelAdmin(admin.ModelAdmin):
    model = PatientHealthModel
    list_display = ['user', 'hb', 'weight', 'sleep_time', 'date']


admin.site.register(PatientHealthModel, PatientHealthModelAdmin)

