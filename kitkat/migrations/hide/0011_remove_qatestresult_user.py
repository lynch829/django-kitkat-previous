# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0010_qatestresult_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qatestresult',
            name='user',
        ),
    ]
