# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 04:08
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Crate', '0001_initial'),
        ('hierarchy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('cc_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
                ('csv', models.CharField(max_length=4)),
                ('expiration_date', models.CharField(max_length=6)),
                ('billing_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('address', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('receives', models.ManyToManyField(to='Crate.Box')),
                ('subscribes_to', models.ManyToManyField(to='hierarchy.InterestGroup')),
            ],
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AlterUniqueTogether(
            name='shippingaddress',
            unique_together=set([('address', 'username')]),
        ),
        migrations.AlterUniqueTogether(
            name='creditcard',
            unique_together=set([('cc_number', 'username')]),
        ),
    ]
