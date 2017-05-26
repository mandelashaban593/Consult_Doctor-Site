# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firebase_cloud_msging', '0003_auto_20161018_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifsclient',
            name='api_key',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
