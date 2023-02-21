from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Patient, Prescription
# Create your views here.


def index(request):
    if checkSession(request):
        template = loader.get_template('dashboard.html')
        context = {
            'attempt': "1",
        }
        return HttpResponse(template.render(context, request))
        # return HttpResponse("dashboard")
    else:
        return redirect("/")
def checkSession(request):
    if "USER_EMAIL" in request.session:
        return True
    else:
        return False

def doctors(request):

    if checkSession(request):
        template = loader.get_template('doctors.html')
        context = {
            'attempt': "1",
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/")


def newpatient(request):
    if checkSession(request):
        query_results = Patient.objects.all()
        template = loader.get_template('newpatient.html')
        context = {
            'attempt': "1",
            'patients': query_results,
        }
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/")


def existingpatient(request):
    if checkSession(request):
        query_results = Patient.objects.all()
        prescriptions = Prescription.objects.all()
        template = loader.get_template('existingpatient.html')
        context = {
            'attempt': "1",
            'patients': query_results,
            'prescriptions': prescriptions
        }
        # return HttpResponse(prescriptions[0].token_number)
        return HttpResponse(template.render(context, request))
    else:
        return redirect("/")

@csrf_exempt
def addnewpatient(request):
    if checkSession(request):
        name = request.POST.get('name')
        cnic = request.POST.get('CNIC')
        fathername = request.POST.get('fathername')
        mobilenumber = request.POST.get('mobilenumber')
        history = request.POST.get('history')
        patient = Patient(patient_name=name, cnic=cnic, father_name=fathername, mobile_number=mobilenumber, history=history)
        patient.save()        

        return existingpatient(request)
    else:
        return redirect("/")

@csrf_exempt
def addnewprescription(request):
    if checkSession(request):
        patientid = request.POST.get('patientid')
        prescr = request.POST.get('prescription')

        patient = Patient.objects.get(pk=patientid)

        prescription = Prescription(patient_id=patient, prescription=prescr)
        prescription.save()        

        return existingpatient(request)
    else:
        return redirect("/")
