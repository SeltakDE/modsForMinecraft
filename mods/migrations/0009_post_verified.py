# Generated by Django 2.2.6 on 2019-10-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0008_auto_20191020_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]