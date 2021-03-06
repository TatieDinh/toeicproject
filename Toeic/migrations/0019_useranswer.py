# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 05:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Toeic', '0018_auto_20160929_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Toeic.Answer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Toeic.Question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Toeic.Test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
