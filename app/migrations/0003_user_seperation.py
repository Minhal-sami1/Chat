# Generated by Django 4.0.2 on 2022-07-14 19:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_user_seperation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='seperation',
            field=models.UUIDField(default=uuid.uuid1, editable=False, unique=True),
        ),
    ]
