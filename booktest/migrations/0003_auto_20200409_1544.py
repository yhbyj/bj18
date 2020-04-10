# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_heroinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='heroinfo',
            old_name='book',
            new_name='hbook',
        ),
    ]
