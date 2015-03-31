# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20150331_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='cleaned_status',
            field=models.IntegerField(default=404),
            preserve_default=False,
        ),
    ]
