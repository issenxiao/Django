# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-24 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
                ('prince', models.CharField(default='￥6', max_length=128)),
            ],
        ),
    ]