# Generated by Django 3.0.6 on 2020-05-17 01:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renewal',
            name='phone_call_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 5, 17, 1, 59, 50, 303295, tzinfo=utc), verbose_name='Phone Call Date'),
        ),
    ]
