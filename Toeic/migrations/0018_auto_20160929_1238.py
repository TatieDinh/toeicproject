# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 05:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Toeic', '0017_useranswer_uservocab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
