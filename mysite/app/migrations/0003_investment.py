# Generated by Django 2.0.6 on 2018-06-14 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_amt', models.DecimalField(decimal_places=6, max_digits=11)),
                ('eth_amt', models.DecimalField(decimal_places=6, max_digits=11)),
                ('xrp_amt', models.DecimalField(decimal_places=6, max_digits=11)),
                ('xlm_amt', models.DecimalField(decimal_places=6, max_digits=11)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('portfolio', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='app.Portfolio')),
            ],
        ),
    ]
