# Generated by Django 4.1.6 on 2023-02-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_telegramuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
