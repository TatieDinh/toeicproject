# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Toeic', '0014_auto_20160922_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='fulltext',
            field=models.TextField(default=''),
        ),
    ]
