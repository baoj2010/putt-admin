# Generated by Django 3.2.9 on 2021-12-25 08:31

from django.db import migrations
import users.queryset


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.queryset.EnhancedUserManager()),
            ],
        ),
    ]