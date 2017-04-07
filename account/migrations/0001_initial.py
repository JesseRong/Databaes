# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 01:08
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Crate', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('interest_id',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Crate.InterestGroup')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('receives', models.ManyToManyField(to='Crate.Box')),
                ('subscribes_to', models.ManyToManyField(to='Crate.InterestGroup')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='shippingaddress',
            unique_together=set([('user_id', 'address')]),
        ),
    ]
