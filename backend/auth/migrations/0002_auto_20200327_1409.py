# Generated by Django 2.2.11 on 2020-03-27 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
    ]
