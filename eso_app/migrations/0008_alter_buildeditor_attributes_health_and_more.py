# Generated by Django 4.1.3 on 2022-11-11 21:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eso_app', '0007_alter_buildeditor_desc_alter_buildeditor_playstyle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildeditor',
            name='attributes_health',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(64), django.core.validators.MinValueValidator(0)], verbose_name='Health'),
        ),
        migrations.AlterField(
            model_name='buildeditor',
            name='attributes_magicka',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(64), django.core.validators.MinValueValidator(0)], verbose_name='Magicka'),
        ),
        migrations.AlterField(
            model_name='buildeditor',
            name='attributes_stamina',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(64), django.core.validators.MinValueValidator(0)], verbose_name='Stamina'),
        ),
    ]
