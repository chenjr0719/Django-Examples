# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(),
        ),
    ]