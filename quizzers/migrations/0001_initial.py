# Generated by Django 3.0.5 on 2020-04-06 20:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizzes_taken', models.IntegerField(default=0)),
                ('quiz_won', models.IntegerField(default=0)),
                ('quiz_loss', models.IntegerField(default=0)),
                ('coins', models.FloatField(default=100.0)),
                ('is_club_creator', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateField(default=datetime.datetime(2020, 4, 6, 20, 10, 3, 505576, tzinfo=utc))),
                ('club_rating', models.FloatField(default=5.0)),
                ('club_admins', models.ManyToManyField(related_name='admins', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
