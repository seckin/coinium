# Generated by Django 2.0.6 on 2018-06-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_investment_original_amt'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='is_approved',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
