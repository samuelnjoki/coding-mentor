# Generated by Django 4.2.7 on 2023-11-16 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentorclub', '0011_alter_user_date_joined_alter_user_last_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='field',
            new_name='course',
        ),
    ]
