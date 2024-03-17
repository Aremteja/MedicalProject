from django import forms
from django.core.exceptions import ValidationError

class PatientRegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    gender = forms.CharField()
    height = forms.IntegerField() # in centimeters
    weight = forms.IntegerField() # in kg

    def clean_password(self):
        pwd = self.cleaned_data['password']
        if not len(pwd) >= 8:
            raise ValidationError('Password length must be greater than or equal to 8. ')
        return pwd
    
    def clean_height(self):
        height = self.cleaned_data['height']
        if height >= 300:
            raise ValidationError('Height should not be greater than 10 feet.')
        return height
    
    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight >= 200:
            raise ValidationError("Weight shouldn't be greater than 200kg")
        return weight
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        pwd = self.cleaned_data['password']
        if len(pwd) < 8:
            raise ValidationError('Password length should be greater than 8 characters.')
        return pwd