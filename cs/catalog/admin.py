from django.contrib import admin
from .models import Patient, Doctor, Prescription
# Register your models here.

# admin.site.register(Patient)
# admin.site.register(Doctor)


class PrecInLine(admin.TabularInline):
    model = Prescription


# define the doctor admin class
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialty')
    inlines = [PrecInLine]


# register the admin class with the associated model
admin.site.register(Doctor, DoctorAdmin)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'first_name', 'last_name')


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'desc')
