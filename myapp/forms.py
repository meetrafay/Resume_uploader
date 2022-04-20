from cProfile import label
from dataclasses import fields
from msilib.schema import RadioButton
from pyexpat import model
from unicodedata import name
from django import forms
from .models import Resume
from django.db import models


GENDER_CHOICES = [

    ('Male', 'Male'),
    ('Female', 'Female')
]

JOB_CITY_CHOICE = [

    ('Karachi', 'Karachi'),
    ('Islamabad', 'Islamabad'),
    ('Lahore', 'Lahore')
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred_job_location', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['id', 'name', 'gender', 'locality', 'city',
                  'pin', 'state', 'mobile','email', 'job_city', 'profile_image', 'my_file']

        labels = {'name': 'Full Name',  'gender': 'Gender', 'locality': 'Location', 'city': 'City', 'pin': 'Pin_Code',
                  'state': 'State', 'mobile': 'Mobile', 'email': 'Email', 'job_city': 'Job_City', 'profile_image': 'Profile_Image', 'my_file': 'Resume'}
        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'dob': forms.DateInput(attrs={'class': 'form-control', 'id':'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),



        }
