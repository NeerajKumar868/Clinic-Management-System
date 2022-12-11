from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput,PasswordInput
from.models import *



class NewUserForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=PasswordInput(
            attrs={
                   'style': 'max-width: 350px;',
                   'class': "form-control",
                   'placeholder':'password',
                  
                   }),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=PasswordInput(
            attrs={
                   'style': 'max-width: 350px;',
                   'class': "form-control",
                   'placeholder':'password',
                  
                   }),
    )


    roles=(('admin',"Nurse"),('customer',"Doctor"))
    role=forms.ChoiceField(widget=forms.RadioSelect,choices=roles)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 350px;',
                'placeholder': 'UserName',
                }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 350px;',
                'placeholder': 'Email'
                }), 
            # 'first_name': TextInput(attrs={
            #     'class': "form-control",
            #     'style': 'max-width: 350px;',
            #     'placeholder': 'Name'
            #     }),
            # 'last_name': TextInput(attrs={
            #     'class': "form-control", 
            #     'style': 'max-width: 350px;',
            #     'placeholder': 'last name'
            #     }), 
        }  