# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-10-07 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0008_train_fare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='Train_Fare',
        ),
    ]
