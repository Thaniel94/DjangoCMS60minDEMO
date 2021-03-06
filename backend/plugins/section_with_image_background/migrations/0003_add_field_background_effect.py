# Generated by Django 2.2.14 on 2020-07-25 18:28

import backend.plugins.section_with_image_background.models
from django.db import migrations
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('section_with_image_background', '0002_add_field_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionwithimagebackgroundpluginmodel',
            name='background_effect',
            field=enumfields.fields.EnumField(blank=True, default=None, enum=backend.plugins.section_with_image_background.models.BackgroundEffect, help_text='Can be applied on top of the image', max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='sectionwithimagebackgroundpluginmodel',
            name='background_effect_color',
            field=enumfields.fields.EnumField(blank=True, default='primary', enum=backend.plugins.section_with_image_background.models.BackgroundEffectColor, max_length=32, null=True),
        ),
    ]
