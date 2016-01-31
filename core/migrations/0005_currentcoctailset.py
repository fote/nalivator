# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160111_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentCoctailSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('cocktail_in_set', models.ForeignKey(to='core.Cocktail')),
            ],
        ),
    ]
