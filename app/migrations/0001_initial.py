# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Edad', models.CharField(max_length=20)),
                ('Telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pasaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clase', models.CharField(max_length=50)),
                ('asiento', models.CharField(max_length=50)),
            ],
        ),
    ]
