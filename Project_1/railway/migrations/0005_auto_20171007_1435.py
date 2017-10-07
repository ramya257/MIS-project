# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-07 14:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0004_auto_20171007_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('Station_Code', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('Station_Name', models.CharField(max_length=30)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stoppage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Arrival_Time', models.TimeField(auto_now_add=True)),
                ('Departure_Time', models.TimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Station_Code', models.ForeignKey(db_column='Station.Station_Code', default='', max_length=5, on_delete=django.db.models.deletion.CASCADE, to='railway.Station')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('Train_No', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=25)),
                ('Seat_Sleeper', models.IntegerField(blank=True)),
                ('Seat_First_Class_AC', models.IntegerField(blank=True)),
                ('Seat_Third_Class_AC', models.IntegerField(blank=True)),
                ('Wifi', models.CharField(max_length=1)),
                ('Food', models.CharField(max_length=1)),
                ('Run_On_Sunday', models.CharField(max_length=1)),
                ('Run_On_Monday', models.CharField(max_length=1)),
                ('Run_On_Tuesday', models.CharField(max_length=1)),
                ('Run_On_Wednesday', models.CharField(max_length=1)),
                ('Run_On_Thursday', models.CharField(max_length=1)),
                ('Run_On_Friday', models.CharField(max_length=1)),
                ('Run_On_Saturday', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='stoppage',
            name='Train_No',
            field=models.ForeignKey(db_column='Train.Train_No', default=0, max_length=6, on_delete=django.db.models.deletion.CASCADE, to='railway.Train'),
        ),
    ]
