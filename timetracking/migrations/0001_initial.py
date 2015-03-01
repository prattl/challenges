# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(default=uuid.uuid1, unique=True, max_length=64)),
                ('title', models.CharField(max_length=120)),
                ('hourly_rate', models.DecimalField(max_digits=7, decimal_places=2)),
                ('tax_rate', models.DecimalField(max_digits=6, decimal_places=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_spent', models.IntegerField(help_text=b'Unit is minutes.')),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('summary', models.CharField(max_length=600)),
                ('job', models.ForeignKey(to='timetracking.Job', to_field=b'uuid')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
