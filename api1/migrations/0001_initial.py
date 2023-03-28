# Generated by Django 4.1.7 on 2023-03-27 19:53

import api1.models
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('job', models.CharField(max_length=50, verbose_name='Job')),
                ('salary', models.DecimalField(decimal_places=2, default=0, max_digits=10, max_length=12, verbose_name='Salary')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to=api1.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Image')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api1.job', verbose_name='Job')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]