# Generated by Django 4.0.6 on 2022-08-08 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_chunkedfile_upload_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chunkedfile',
            name='upload_time',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 8, 9, 0, 26, 41, 868218)),
        ),
    ]
