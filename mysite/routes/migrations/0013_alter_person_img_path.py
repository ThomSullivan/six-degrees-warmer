# Generated by Django 3.2.6 on 2021-08-25 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0012_alter_movie_img_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='img_path',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
