# Generated by Django 2.0.6 on 2018-07-02 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180702_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='experience',
            field=models.CharField(default='', max_length=250),
        ),
    ]
