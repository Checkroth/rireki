# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_name', models.CharField(max_length=255)),
                ('main_description', models.CharField(max_length=255)),
                ('site', models.OneToOneField(to='sites.Site')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
