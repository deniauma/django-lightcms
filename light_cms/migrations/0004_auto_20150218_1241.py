# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('light_cms', '0003_article_article_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('validated', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('calendar_title', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_monday_opened', models.BooleanField(default=False)),
                ('monday_start', models.TimeField()),
                ('monday_end', models.TimeField()),
                ('is_tuesday_opened', models.BooleanField(default=False)),
                ('tuesday_start', models.TimeField()),
                ('tuesday_end', models.TimeField()),
                ('is_wednesday_opened', models.BooleanField(default=False)),
                ('wednesday_start', models.TimeField()),
                ('wednesday_end', models.TimeField()),
                ('is_thursday_opened', models.BooleanField(default=False)),
                ('thursday_start', models.TimeField()),
                ('thursday_end', models.TimeField()),
                ('is_friday_opened', models.BooleanField(default=False)),
                ('friday_start', models.TimeField()),
                ('friday_end', models.TimeField()),
                ('is_saturday_opened', models.BooleanField(default=False)),
                ('saturday_start', models.TimeField()),
                ('saturday_end', models.TimeField()),
                ('is_sunday_opened', models.BooleanField(default=False)),
                ('sunday_start', models.TimeField()),
                ('sunday_end', models.TimeField()),
                ('calendar', models.ForeignKey(to='light_cms.Calendar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Unavailabilities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('label', models.CharField(max_length=200)),
                ('calendar', models.ForeignKey(to='light_cms.Calendar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appointment',
            name='calendar',
            field=models.ForeignKey(to='light_cms.Calendar'),
            preserve_default=True,
        ),
    ]
