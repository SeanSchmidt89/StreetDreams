# Generated by Django 4.0.4 on 2022-05-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetdreams_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
