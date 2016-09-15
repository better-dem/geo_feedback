# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aesthetic_pref', models.BooleanField(default=False)),
                ('transportation_pref', models.BooleanField(default=False)),
            ],
        ),
    ]