# Generated by Django 4.1.3 on 2022-11-12 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eso_app', '0013_alter_races_alliance_alter_zones_alliance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='races',
            name='alliance',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='eso_app.alliances'),
        ),
    ]
