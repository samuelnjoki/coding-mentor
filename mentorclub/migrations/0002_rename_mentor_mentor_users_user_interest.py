# Generated by Django 4.2.7 on 2023-11-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorclub', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='mentor',
            new_name='users',
        ),
        migrations.AddField(
            model_name='user',
            name='interest',
            field=models.CharField(default='mentor', max_length=10),
            preserve_default=False,
        ),
    ]
