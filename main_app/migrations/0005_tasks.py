# Generated by Django 4.2 on 2023-04-20 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_myfestivalplanning_myfestival'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('completed', models.BooleanField()),
                ('due_date', models.DateField()),
            ],
        ),
    ]
