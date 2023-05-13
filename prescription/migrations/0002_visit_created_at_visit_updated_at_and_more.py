# Generated by Django 4.1.6 on 2023-05-13 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]