# Generated by Django 2.1.2 on 2018-11-10 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_prescription_dop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='hospital',
            name='depart',
            field=models.CharField(help_text='Enter the hospital department: ', max_length=25, null=True, verbose_name='Hospital Dept'),
        ),
    ]
