# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160111_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='ing2',
            field=models.ForeignKey(blank=True, null=True, related_name='ing2', to='core.Beverage'),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='ing3',
            field=models.ForeignKey(blank=True, null=True, related_name='ing3', to='core.Beverage'),
        ),
    ]
