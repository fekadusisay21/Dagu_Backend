# Generated by Django 5.0.2 on 2024-03-24 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0004_newsarticle_rename_follower_follow_follower_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='url',
        ),
    ]
