# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-09 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_isguest'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='isFinished',
            field=models.BooleanField(default=False, verbose_name='Tamamland\u0131 M\u0131 ?/Is Finished'),
        ),
    ]
