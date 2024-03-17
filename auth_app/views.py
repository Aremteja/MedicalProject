from django.shortcuts import render
from .models import User
from .forms import PatientRegistrationForm, LoginForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout


def patient_registration(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create_user(**form.cleaned_data)
                return redirect(reverse('auth_app:login'))
            except :
                return render(request, 'auth_app/registration.html', {'form':form, 'error':'Username Already taken'})
        else:
            return render(request, 'auth_app/registration.html', {'form':form})
    else:
        form = PatientRegistrationForm()
    return render(request, 'auth_app/registration.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect(reverse('patient_app:data_entry'))
            else:
                error = "Invalid credentials"
                return render(request, 'auth_app/login.html', {'form':form,'error':error})
        else:
            return render(request, 'auth_app/login.html', {'form':form})
    form = LoginForm() 
    return render(request, 'auth_app/login.html', {'form':form})
        

def logout_view(request):
    logout(request)
    return redirect(reverse('auth_app:login'))
