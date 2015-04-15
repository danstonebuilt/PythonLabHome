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
                ('raffle_nbr', models.CharField(max_length=6)),
                ('day_of_week', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('nbr_01', models.IntegerField(default=0)),
                ('nbr_02', models.IntegerField(default=0)),
                ('nbr_03', models.IntegerField(default=0)),
                ('nbr_04', models.IntegerField(default=0)),
                ('nbr_05', models.IntegerField(default=0)),
                ('nbr_06', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
