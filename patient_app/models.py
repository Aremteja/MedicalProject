from django.db import models
from auth_app.models import User


class PatientHealthModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hb = models.IntegerField(verbose_name='Heart Beat')
    weight = models.IntegerField()
    sleep_time = models.TimeField()
    date = models.DateTimeField(auto_now_add=True)
    
