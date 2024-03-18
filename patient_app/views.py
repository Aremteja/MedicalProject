from django.shortcuts import render
import pandas as pd
from .models import PatientHealthModel
from .forms import PatientDataForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from datetime import datetime
from .ml_model import MLModel
from MedicalProject.settings import BASE_DIR
from .utils import cleaning_latest_record
import numpy as np


def index(request):
    return render(request, 'patient_app/index.html')


@login_required(login_url=reverse_lazy('auth_app:login'))
def patient_data_enter_view(request):
    if request.method == "POST":
        form = PatientDataForm(request.POST)
        if form.is_valid():
            user = request.user
            PatientHealthModel.objects.create(**{'user':user, **form.cleaned_data})
            return redirect(reverse('patient_app:dashboard'))
        else:
            return render(request, 'patient_app/patient_data_form.html', {'form':form})
    form = PatientDataForm()
    return render(request, 'patient_app/patient_data_form.html', {'form':form})


@login_required(login_url=reverse_lazy('auth_app:login'))
def patient_dashboard(request):
    # getting the active user
    user = request.user
    # Extracting the PatientHealthModel Data of that particular user
    patient_data = PatientHealthModel.objects.filter(user=user)

    
    # checking whether the user has PatientHealthModel data or not if not displaying the dashboard with out any data
    if not patient_data.exists():
        return render(request, 'patient_app/dashboard.html', {'rating':0})
    
    
    # columns for pandas data frame
    columns = ['hb', 'sleep_time', 'date', 'weight']
    df = pd.DataFrame(patient_data.values_list('hb', 'sleep_time', 'date', 'weight'), columns=columns)
    
    # sorting values to remove the old records of that particular day
    df.sort_values(by='date', ascending=True)
    # after sorting changing the date as per our requirement
    df['date'] = [ x.date() for x in df['date']]

    # removing the old records of that particular day
    df = df.drop_duplicates(subset='date') 
    
    # finding the latest record
    df_latest_record = df.tail(1)

    x = df_latest_record.to_dict()
    
    # converting it into dict
    latest_record = cleaning_latest_record(x)
    
    # age of the person
    age = datetime.today().year - request.user.dob.year
    
    # Define the the path to your model file
    model_path = BASE_DIR/'ml_models'/'project_model.h5'

    # creating the MLModel object
    ml_model_prediction = MLModel(model_path=model_path)
    
    # input data to the MLModel
    # inputs are => heart_beat, BMI, gender, sleep time, age
    input_data = np.array([[
        latest_record['hb'],
        int(latest_record['weight']/((user.height/100)**2)),
        1 if user.gender == 'M' else 0,
        latest_record['sleep_time'].hour,
        age
    ]])
    
    # prediction determined by the Machine Learning Model
    rating_prediction = ml_model_prediction.predict(input_data)
    rating = np.argmax(rating_prediction) + 1

    # converting sleep time into hours for displaying in charts
    df['sleep_time'] = [x.hour for x in df['sleep_time'] ]
        
    return render(request, 'patient_app/dashboard.html', {'data': df.to_json(orient='records', date_format='iso'), 'rating':rating})
