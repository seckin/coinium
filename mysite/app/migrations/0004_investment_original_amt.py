# Generated by Django 2.0.6 on 2018-06-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_investment'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='original_amt',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10),
            preserve_default=False,
        ),
    ]