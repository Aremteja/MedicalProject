from django import forms
from django.core.exceptions import ValidationError


class PatientDataForm(forms.Form):
    hb = forms.IntegerField()
    weight = forms.IntegerField()
    sleep_time = forms.TimeField()

    def clean_sleep_time(self):
        sleep_time = self.cleaned_data['sleep_time']
        if sleep_time.hour >= 24:
            raise ValidationError("Sleep time can't be greater than 24 hours.")
        return sleep_time
    