# Generated by Django 4.1.2 on 2022-11-05 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eso_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Character',
            new_name='Characters',
        ),
        migrations.RenameModel(
            old_name='DLC',
            new_name='DLCs',
        ),
        migrations.RenameModel(
            old_name='MonsterSet',
            new_name='MonsterSets',
        ),
        migrations.RenameModel(
            old_name='Mythic',
            new_name='Mythics',
        ),
        migrations.RenameModel(
            old_name='Role',
            new_name='Roles',
        ),
    ]
