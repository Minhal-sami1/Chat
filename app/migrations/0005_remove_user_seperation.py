# Generated by Django 4.0.2 on 2022-07-14 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_user_seperation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='seperation',
        ),
    ]
