# Generated by Django 2.0.6 on 2018-06-24 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180624_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='_0xBTC_pct',
            new_name='e_0xBTC_pct',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='_1337_pct',
            new_name='e_1337_pct',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='_1ST_pct',
            new_name='e_1ST_pct',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='_1WO_pct',
            new_name='e_1WO_pct',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='_2GIVE_pct',
            new_name='e_2GIVE_pct',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='_42_pct',
            new_name='e_42_pct',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='_808_pct',
            new_name='e_808_pct',
        ),
    ]