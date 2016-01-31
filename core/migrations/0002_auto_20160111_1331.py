# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beverages',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, default='')),
                ('alc', models.PositiveSmallIntegerField(blank=True)),
                ('density', models.PositiveSmallIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cocktails',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, default='')),
                ('ing1_p', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ing2_p', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ing3_p', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
