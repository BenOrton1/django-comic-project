# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-27 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0005_commition_yourname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commition',
            name='colour',
            field=models.CharField(choices=[('line art only', 'line art only'), ('black and white', 'black and white'), ('full colour', 'full colour')], default='line art only', max_length=2),
        ),
    ]