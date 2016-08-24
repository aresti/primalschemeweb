# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='fasta',
            field=models.FileField(help_text='One or more viral reference genomes in FASTA format', upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
