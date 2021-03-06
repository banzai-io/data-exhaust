# Generated by Django 3.1.3 on 2020-11-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signal_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasignal',
            name='signal_meta',
            field=models.JSONField(blank=True, help_text='Contains event and contact data e.g. seniority, job options', null=True, verbose_name='Signal Meta Data'),
        ),
        migrations.AlterField(
            model_name='datasignal',
            name='valid',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
