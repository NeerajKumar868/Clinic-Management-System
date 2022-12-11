from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    patient_list=Patient.objects.all()
    total=patient_list.count()
  
    contaxt={
        'patient_list':patient_list,
        'total':total,


    }
    return render(request,"crudapp/home.html",contaxt)


def delete(request,id):
    patient_list=Patient.objects.filter(patient_id=id)
    patient_list.delete() 
    return redirect('/crudapp')


@login_required()
def save(request):
    if request.method=="GET":
        return render(request,"crudapp/form.html",{'action':'save'})
    elif request.method=="POST":
        patient_name=request.POST['patient_name']
        patient_age=request.POST['patient_age']
        patient_gender=request.POST['patient_gender']
        patient_location=request.POST['patient_location']
        patient_date_of_visit=request.POST['patient_date_of_visit']
        patient_reason_to_visit=request.POST['patient_reason_to_visit']
        patient_obj=Patient.objects.create(patient_name=patient_name,patient_age=patient_age,patient_gender=patient_gender,patient_location=patient_location,patient_date_of_visit=patient_date_of_visit,patient_reason_to_visit=patient_reason_to_visit)
        patient_obj.save()
        return redirect('/crudapp')