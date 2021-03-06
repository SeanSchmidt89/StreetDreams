# Generated by Django 4.0.4 on 2022-05-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetdreams_app', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='car',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mods',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]
