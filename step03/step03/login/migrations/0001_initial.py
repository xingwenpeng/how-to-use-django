# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pr',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('photo_id', models.CharField(max_length=20)),
                ('photo_path', models.CharField(max_length=200)),
                ('photo_size', models.IntegerField()),
                ('photo_type', models.CharField(max_length=8)),
                ('browse_times', models.IntegerField(default=1)),
                ('user_name', models.CharField(max_length=30, default=None)),
                ('photo_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_register',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=30, default=None)),
                ('user_passwd', models.CharField(max_length=30, default=None)),
                ('user_email', models.EmailField(max_length=254, default=None)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
