# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='output_prefix',
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Scheme name'),
        ),
    ]
