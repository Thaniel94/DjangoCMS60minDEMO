# Generated by Django 2.2.12 on 2020-05-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailchimp', '0003_allow_border_enabling'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailchimppluginmodel',
            name='width',
            field=models.CharField(default='100%', help_text='In css format, eg 350px or 100%', max_length=512),
        ),
    ]
