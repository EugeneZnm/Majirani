# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbours', '0009_auto_20181024_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='neighbours.Profile'),
        ),
    ]
