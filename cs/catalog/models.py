from django.db import models


class Patient(models.Model):
    # model representing patient
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    ssn = models.IntegerField('SSN', blank=False, primary_key=True)
    first_name = models.CharField('First Name', max_length=50, blank=False)
    last_name = models.CharField('Last Name', max_length=50, blank=False)
    insurance = models.CharField('Insurance', max_length=50, blank=False)
    insurance_num = models.IntegerField('Insurance Number', blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

