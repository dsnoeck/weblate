# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-09 13:49
from __future__ import unicode_literals

import os
import binascii

from django.conf import settings
from django.db import migrations


def run_migration(apps, schema_editor):
    """Ensure all users have unique emails."""
    User = apps.get_model('weblate_auth', 'User')
    # These all were used for deleted or anonymous users at some point
    emails = ('', 'noreply@example.com', 'noreply@weblate.org')
    for user in User.objects.filter(email__in=emails):
        if user.username == settings.ANONYMOUS_USER_NAME:
            user.email = 'noreply@weblate.org'
        else:
            user.email = 'noreply+{}-{}@weblate.org'.format(
                user.pk,
                binascii.b2a_hex(os.urandom(5))
            )
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('weblate_auth', '0007_auto_20180509_0739'),
    ]

    operations = [
        migrations.RunPython(run_migration)
    ]
