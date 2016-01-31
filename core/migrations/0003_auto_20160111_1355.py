# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160111_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('ing1_p', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ing2_p', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('ing3_p', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Beverages',
            new_name='Beverage',
        ),
        migrations.DeleteModel(
            name='Cocktails',
        ),
        migrations.AddField(
            model_name='cocktail',
            name='ing1',
            field=models.ForeignKey(related_name='ing1', to='core.Beverage'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='ing2',
            field=models.ForeignKey(related_name='ing2', to='core.Beverage'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='ing3',
            field=models.ForeignKey(related_name='ing3', to='core.Beverage'),
        ),
    ]
