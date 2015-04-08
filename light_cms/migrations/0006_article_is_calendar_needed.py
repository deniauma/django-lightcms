# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('light_cms', '0005_auto_20150218_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_calendar_needed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
