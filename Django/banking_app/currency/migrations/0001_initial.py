# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-26 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CurrName', models.CharField(max_length=10)),
                ('CurrCode', models.IntegerField(max_length=10)),
                ('id_number', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'tbl_currency',
                'managed': True,
            },
        ),
    ]