# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='questions.Answer'),
        ),
    ]
