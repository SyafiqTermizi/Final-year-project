# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment_analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword_tweets',
            name='geo_location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='keyword_tweets',
            name='no_of_rt',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='keyword_tweets',
            name='reply_to_tweet_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='keyword_tweets',
            name='reply_to_user_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_tweets',
            name='geo_location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_tweets',
            name='no_of_rt',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_tweets',
            name='reply_to_tweet_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_tweets',
            name='reply_to_user_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
