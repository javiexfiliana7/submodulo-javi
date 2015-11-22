# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='asunt',
            field=models.CharField(default='nada', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.CharField(default='nada', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='descrip',
            field=models.CharField(default='nada', max_length=200),
            preserve_default=False,
        ),
    ]
