# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20160121_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='in_work',
            field=models.BooleanField(default=False),
        ),
    ]
