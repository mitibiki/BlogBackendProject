# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-15 08:23
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestprofile',
            name='is_subcribe',
            field=models.BooleanField(default=True, help_text='除验证码通知邮件外的通知邮件', verbose_name='是否订阅通知邮件'),
        ),
        migrations.AddField(
            model_name='guestprofile',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True, help_text='发送时间', null=True, verbose_name='发送时间'),
        ),
    ]