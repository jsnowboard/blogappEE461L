# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_postcontent_is_revision_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='active_revision_id',
            field=models.IntegerField(default=0),
        ),
    ]
