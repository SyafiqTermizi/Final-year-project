# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-24 05:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword_search',
            fields=[
                ('keyword', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('search_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Keyword_tweets',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField()),
                ('tweet_text', models.CharField(max_length=140)),
                ('reply_to_tweet_id', models.BigIntegerField()),
                ('reply_to_user_id', models.BigIntegerField()),
                ('geo_location', models.CharField(max_length=200)),
                ('user_verified', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('user_screen_name', models.CharField(max_length=200)),
                ('no_of_rt', models.IntegerField()),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentiment_analysis.Keyword_search')),
            ],
        ),
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('screen_name', models.CharField(max_length=200)),
                ('verified', models.BooleanField()),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
                ('no_of_tweets', models.IntegerField()),
                ('favourites_count', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('joined_twitter', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user_tweets',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tweet_text', models.CharField(max_length=140)),
                ('reply_to_tweet_id', models.BigIntegerField()),
                ('reply_to_user_id', models.BigIntegerField()),
                ('geo_location', models.CharField(max_length=200)),
                ('user_verified', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('user_screen_name', models.CharField(max_length=200)),
                ('no_of_rt', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentiment_analysis.User_details')),
            ],
        ),
    ]