# Generated by Django 4.2 on 2023-04-20 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_tasks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
