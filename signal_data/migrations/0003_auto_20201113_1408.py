# Generated by Django 3.1.3 on 2020-11-13 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signal_data', '0002_auto_20201113_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasignal',
            old_name='hashed_identifier',
            new_name='identifier',
        ),
    ]