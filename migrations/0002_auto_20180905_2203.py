# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-05 14:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserInfo',
            new_name='User',
        ),
    ]
