# Generated by Django 4.2.7 on 2023-12-06 16:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0008_todousezprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToDoUsezProfile',
            new_name='ToDoUserProfile',
        ),
    ]
