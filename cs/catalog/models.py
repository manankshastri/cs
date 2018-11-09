from django.db import models


class Patient(models.Model):
    # model representing patient
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    ssn = models.IntegerField('SSN', blank=False, primary_key=True)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Doctor(models.Model):
    # model representing doctor
    PREFIX = [('Dr', 'Dr')]
    ssn = models.IntegerField('SSN', blank=False, primary_key=True)
    prefix = models.CharField(max_length=2, choices=PREFIX)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    specialty = models.CharField(max_length=50)
    # patient = models.ManyToManyField(Patient)
    # description = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Prescription(models.Model):
    # model representing prescription
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    desc = models.TextField('Prescription', help_text='Enter the prescription : ')

    def __str__(self):
        return f'{self.patient} {self.doctor} {self.desc}'

