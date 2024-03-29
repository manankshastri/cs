# Generated by Django 2.1.2 on 2018-10-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('ssn', models.IntegerField(max_length=10, primary_key=True, serialize=False, verbose_name='SSN')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('insurance', models.CharField(max_length=50, verbose_name='Insurance')),
                ('insurance_num', models.IntegerField(max_length=50, verbose_name='Insurance Number')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
    ]
