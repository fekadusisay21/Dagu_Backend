# Generated by Django 5.0.2 on 2024-03-24 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_alter_news_options_alter_topics_options_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=100)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.URLField()),
                ('url_to_image', models.URLField(blank=True, null=True)),
                ('published_at', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='Follower',
            new_name='follower',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='Following',
            new_name='following',
        ),
        migrations.AddField(
            model_name='news',
            name='news_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='News.newsarticle'),
        ),
    ]
