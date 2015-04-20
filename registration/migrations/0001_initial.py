# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, verbose_name='activation key')),
                ('verified', models.BooleanField(default=False, verbose_name='verified')),
                ('activated', models.BooleanField(default=False, verbose_name='activated')),
                ('moderated', models.BooleanField(default=False, verbose_name='moderated')),
                ('moderation_time', models.DateTimeField(null=True, verbose_name='moderation_time')),
                ('moderator', models.ForeignKey(related_name='moderated_profiles', verbose_name='moderator', to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.OneToOneField(related_name='registration_profile', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'registration profile',
                'verbose_name_plural': 'registration profiles',
            },
        ),
    ]
