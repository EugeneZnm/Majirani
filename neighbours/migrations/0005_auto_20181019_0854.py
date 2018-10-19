# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighbours', '0004_neighbourhood_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='user',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Neighbourhood', to='neighbours.Profile'),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='biz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Business', to='neighbours.Business'),
        ),
        migrations.AlterField(
            model_name='business',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbours.Profile'),
        ),
    ]
