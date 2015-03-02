# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('timetracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeentry',
            options={'verbose_name': 'Time Entry', 'verbose_name_plural': 'Time Entries'},
        ),
        migrations.AlterField(
            model_name='job',
            name='uuid',
            field=models.CharField(default=uuid.uuid1, unique=True, max_length=64, editable=False),
            preserve_default=True,
        ),
    ]
