# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_currentcoctailset'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentPumpSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pump1', models.ForeignKey(null=True, related_name='pump1', blank=True, to='core.Beverage')),
                ('pump2', models.ForeignKey(null=True, related_name='pump2', blank=True, to='core.Beverage')),
                ('pump3', models.ForeignKey(null=True, related_name='pump3', blank=True, to='core.Beverage')),
            ],
        ),
    ]
