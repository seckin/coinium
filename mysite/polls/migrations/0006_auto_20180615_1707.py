# Generated by Django 2.0.6 on 2018-06-15 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_investment_is_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investment',
            old_name='is_approved',
            new_name='is_active',
        ),
    ]