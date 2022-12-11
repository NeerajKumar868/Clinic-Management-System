from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


admingrp = Group.objects.get(name='admin')
customergrp = Group.objects.get(name="customer")


def homepage(request):
    return render(request, 'registration/index.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        role=request.POST['role']
        if form.is_valid():
            userobj = form.save()
            login(request, userobj)
            if role=="admin":
                userobj.groups.add(admingrp)
            elif role=="customer":
                userobj.groups.add(customergrp) 
            messages.success(request, "Registration successful." )
            return redirect("homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request,'registration/register.html', context={"register_form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        # AuthenticationForm_can_also_be_used__
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                form = login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, f'account done not exit plz sign in')
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})


def logout_request(request):
    logout(request)
    messages.info(request, "logged out.") 
    return redirect("homepage")
