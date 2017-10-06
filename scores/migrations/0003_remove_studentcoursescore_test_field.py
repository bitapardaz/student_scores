# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_studentcoursescore_test_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentcoursescore',
            name='test_field',
        ),
    ]
