# Generated by Django 2.0.6 on 2018-07-02 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180701_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investor',
            old_name='city',
            new_name='location',
        ),
    ]