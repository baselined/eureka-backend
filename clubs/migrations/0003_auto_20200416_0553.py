# Generated by Django 3.0.5 on 2020-04-16 00:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20200412_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 4, 16, 0, 23, 21, 320794, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='joinrequest',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 4, 16, 0, 23, 21, 321434, tzinfo=utc)),
        ),
    ]
