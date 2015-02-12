# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('light_cms', '0002_article_is_main_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_slug',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
