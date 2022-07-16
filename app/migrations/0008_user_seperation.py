# Generated by Django 4.0.2 on 2022-07-14 20:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_user_seperation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='seperation',
            field=models.CharField(default=uuid.uuid1, editable=False, max_length=2, unique=True),
        ),
    ]
