# Generated by Django 3.0.5 on 2020-04-16 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20200416_0556'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answer',
            new_name='Option',
        ),
    ]