# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_auto_20170528_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(related_name='perfil', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
