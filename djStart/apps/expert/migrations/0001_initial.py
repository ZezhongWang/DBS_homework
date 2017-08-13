# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 10:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='message.User', verbose_name='用户帐号')),
                ('expert_number', models.CharField(blank=True, max_length=8, null=True, verbose_name='专家证书编号')),
                ('valid_time', models.DateField(blank=True, null=True, verbose_name='证书有效时间')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='证书有效时间')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=10)),
                ('birthday', models.DateField(verbose_name='出生日期')),
                ('politic', models.CharField(max_length=20, verbose_name='政治面貌')),
                ('certificate_type', models.CharField(max_length=20, verbose_name='证件类型')),
                ('certificate_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='证件号')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='电话号码')),
                ('email', models.EmailField(blank=True, max_length=20, null=True, verbose_name='邮箱')),
                ('pic', models.ImageField(default='image/default/', upload_to='image/%Y/%m', verbose_name='照片')),
            ],
            options={
                'verbose_name': '专家信息表',
                'db_table': 'Expert',
                'verbose_name_plural': '专家信息表',
            },
        ),
    ]