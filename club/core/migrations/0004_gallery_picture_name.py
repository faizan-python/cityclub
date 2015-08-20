# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='picture_name',
            field=models.CharField(default='abc', max_length=128),
            preserve_default=False,
        ),
    ]
