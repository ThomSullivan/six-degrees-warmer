# Generated by Django 3.2.6 on 2021-08-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_profile_favorite_bacon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite_bacon',
            field=models.TextField(default='', null=True),
        ),
    ]