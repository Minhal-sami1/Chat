# Generated by Django 4.0.2 on 2022-08-08 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacted_people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FROM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FROM', to=settings.AUTH_USER_MODEL)),
                ('TO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TO', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
