# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-26 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuzo', '0002_auto_20190526_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
