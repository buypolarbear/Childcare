# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20161104_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin_log',
            name='in_class',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='access_level',
            field=models.CharField(choices=[('e', 'Employee'), ('p', 'Parent')], default='e', max_length=2),
        ),
        migrations.AlterField(
            model_name='child',
            name='status',
            field=models.BooleanField(choices=[('Dropped Off', True), ('Picked Up', False)], default=False),
        ),
    ]
