# Generated by Django 5.0.3 on 2024-03-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_codes', '0002_remove_chatroom_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
