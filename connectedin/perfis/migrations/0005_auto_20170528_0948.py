# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_auto_20170528_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(related_name='perfis', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
