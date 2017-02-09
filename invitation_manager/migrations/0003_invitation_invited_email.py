# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invitation_manager', '0002_invitation_invitation_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='invited_email',
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
    ]
