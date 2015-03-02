# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracking', '0002_auto_20150302_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='tax_rate',
            field=models.DecimalField(help_text=b'Unit is %', max_digits=6, decimal_places=4),
            preserve_default=True,
        ),
    ]
