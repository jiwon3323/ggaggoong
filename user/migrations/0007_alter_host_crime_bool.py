# Generated by Django 3.2.8 on 2021-11-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20211108_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='crime_bool',
            field=models.BooleanField(default=False),
        ),
    ]
