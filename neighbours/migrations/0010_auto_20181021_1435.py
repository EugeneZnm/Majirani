# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbours', '0009_auto_20181021_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='description',
            field=models.CharField(max_length=15000, null=True),
        ),
    ]
