# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Toeic', '0002_vocab'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('text', models.TextField(default='add content')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Toeic.Level')),
                ('topics', models.ManyToManyField(to='Toeic.Topic')),
                ('vocabs', models.ManyToManyField(to='Toeic.Vocab')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('text', models.TextField(default='')),
                ('url', models.URLField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Toeic.Level')),
                ('topics', models.ManyToManyField(to='Toeic.Topic')),
                ('vocabs', models.ManyToManyField(to='Toeic.Vocab')),
            ],
        ),
    ]