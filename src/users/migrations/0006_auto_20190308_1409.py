# Generated by Django 2.1.5 on 2019-03-08 14:09

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190308_1127'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('objects', users.models.UserProfileManager()),
            ],
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='users',
        ),
    ]
