# Generated by Django 2.1.2 on 2018-10-31 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20181030_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('ssn', models.IntegerField(primary_key=True, serialize=False, verbose_name='SSN')),
                ('prefix', models.CharField(choices=[('Dr', 'Dr')], max_length=2)),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('specialty', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='insurance',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='insurance_num',
        ),
        migrations.AddField(
            model_name='patient',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='patient',
            field=models.ManyToManyField(to='catalog.Patient'),
        ),
    ]
