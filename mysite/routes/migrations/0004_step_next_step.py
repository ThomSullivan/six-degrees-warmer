# Generated by Django 3.2.6 on 2021-08-09 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_remove_step_next_step'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='next_step',
            field=models.ForeignKey(default=4724, on_delete=django.db.models.deletion.CASCADE, related_name='next_step_person', to='routes.person'),
        ),
    ]
