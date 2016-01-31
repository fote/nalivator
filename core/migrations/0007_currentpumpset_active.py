# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_currentpumpset'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentpumpset',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
