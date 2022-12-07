# Generated by Django 4.1.3 on 2022-12-07 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='channel',
            field=models.ForeignKey(default='Anonymus', on_delete=django.db.models.deletion.CASCADE, related_name='video_channel', to='projectapp.channel'),
        ),
    ]