# Generated by Django 4.1.3 on 2022-11-11 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eso_app', '0009_alter_buildeditor_mundus'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildeditor',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=20),
        ),
    ]