# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='pic_url',
            field=models.CharField(default='http://img.mictester.com', max_length=128),
            preserve_default=False,
        ),
    ]
