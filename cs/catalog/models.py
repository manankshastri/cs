from django.db import models


class Patient(models.Model):
    # model representing patient
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    ssn = models.IntegerField('SSN', blank=False, primary_key=True)
    title = models.CharField(max_length=10, blank=True)
    suffix = models.CharField(max_length=4, blank=True)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateTimeField('Date of Birth')
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    email = models.EmailField()
    # race = models.CharField(max_length=20)
    # language = models.CharField(max_length=30)
    insurance = models.CharField('Health Insurance Carrier', max_length=50, blank=False)
    credit_card = models.CharField(max_length=30, blank=False)
    credit_card_number = models.IntegerField(blank=False)
    description = models.TextField()
    doctor = models.ManyToManyField('Doctor', blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Doctor(models.Model):
    # model representing doctor
    PREFIX = [('Dr', 'Dr')]
    prefix = models.CharField(max_length=1, choices=PREFIX, blank=False)
    first_name = models.CharField('First Name', max_length=50, blank=False)
    last_name = models.CharField('Last Name', max_length=50, blank=False)



