# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150928_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcontent',
            name='is_revision_active',
        ),
    ]
