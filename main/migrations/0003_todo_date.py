# Generated by Django 3.2.9 on 2021-12-15 08:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_todo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 15, 8, 0, 33, 576926, tzinfo=utc)),
        ),
    ]
