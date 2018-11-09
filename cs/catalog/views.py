from django.shortcuts import render
from .models import Patient, Doctor, Prescription


# Create your views here.
def index(request):
    """ view function for home page"""

    # generate number of patients
    num_patients = Patient.objects.all().count()

    # generate number of doctors
    num_doctors = Doctor.objects.all().count()

    context = {
        'num_patients': num_patients,
        'num_doctors': num_doctors,
    }

    # render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
