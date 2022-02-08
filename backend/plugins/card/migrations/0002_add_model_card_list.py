# Generated by Django 2.2.12 on 2020-06-05 15:42

import backend.plugins.card.models
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardListPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='card_cardlistpluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('cards_per_row', enumfields.fields.EnumField(default='3', enum=backend.plugins.card.models.CardsPerRow, max_length=32)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]