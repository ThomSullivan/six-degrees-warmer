# Generated by Django 3.2.6 on 2021-08-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0005_auto_20210816_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='fav',
            name='bacon_number',
            field=models.IntegerField(default='4', null=True),
        ),
    ]