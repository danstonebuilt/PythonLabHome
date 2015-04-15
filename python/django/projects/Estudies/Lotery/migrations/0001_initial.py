# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Megasena',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('raffleNumber', models.CharField(max_length=10)),
                ('dayOfWeak', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=50)),
                ('n1', models.CharField(max_length=2)),
                ('n2', models.CharField(max_length=2)),
                ('n3', models.CharField(max_length=2)),
                ('n4', models.CharField(max_length=2)),
                ('n5', models.CharField(max_length=2)),
                ('n6', models.CharField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
