# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postcontent_revision_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcontent',
            name='is_revision_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 28, 17, 8, 53, 614640, tzinfo=utc), verbose_name='date published'),
        ),
    ]
