# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_active_revision_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcontent',
            name='revision_name',
        ),
        migrations.AddField(
            model_name='postcontent',
            name='is_active_revision',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postcontent',
            name='revision_number',
            field=models.IntegerField(default=0),
        ),
    ]
