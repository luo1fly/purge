# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_history_pic_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='cleaned_by',
            field=models.ForeignKey(to='app01.OptUser'),
            preserve_default=True,
        ),
    ]
