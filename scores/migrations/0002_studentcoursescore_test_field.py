# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcoursescore',
            name='test_field',
            field=models.IntegerField(default=0),
        ),
    ]