# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-26 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20210324_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='addr',
            field=models.CharField(default='BeijingRoad', max_length=128),
        ),
    ]
