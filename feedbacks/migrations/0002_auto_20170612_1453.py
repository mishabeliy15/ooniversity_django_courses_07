# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='from_email',
            field=models.EmailField(default=2, max_length=254, verbose_name='email отправителя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(verbose_name='текст сообщения'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=255, verbose_name='имя отправителя'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='тема сообщения'),
        ),
    ]
