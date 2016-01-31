# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_currentpumpset_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='name',
            field=models.CharField(unique=True, max_length=128, default=''),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='name',
            field=models.CharField(unique=True, max_length=128, default=''),
        ),
    ]
