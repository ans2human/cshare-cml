# Generated by Django 2.2.7 on 2019-12-02 05:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191202_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 12, 2, 5, 35, 29, 960414, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
