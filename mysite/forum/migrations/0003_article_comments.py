# Generated by Django 3.2.6 on 2021-08-17 14:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comments',
            field=models.ManyToManyField(related_name='article_comments', through='forum.Comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
