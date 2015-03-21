# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_message_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 3, 21, 20, 54, 24, 662736, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
