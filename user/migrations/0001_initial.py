# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-16 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('user_authority', models.IntegerField(choices=[(0, 'normal'), (1, 'admin')], default=0)),
            ],
        ),
    ]
