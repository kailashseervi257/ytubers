# Generated by Django 3.1.4 on 2021-01-03 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0003_auto_20210103_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretubers',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 3, 16, 3, 33, 36652)),
        ),
    ]
