# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-27 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0009_auto_20190927_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='commition',
            name='colour',
            field=models.CharField(choices=[('Line art only', 'Line art only'), ('Black and white', 'Black and white'), ('Full colour', 'Full colour')], default='Line art only', max_length=40),
        ),
        migrations.AddField(
            model_name='commition',
            name='cover',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=40),
        ),
    ]