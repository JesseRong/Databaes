# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Crate', '0001_initial'),
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hierarchy.InterestGroup'),
        ),
    ]
