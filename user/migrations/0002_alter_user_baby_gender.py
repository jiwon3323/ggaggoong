# Generated by Django 3.2.8 on 2021-10-28 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='baby_gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=80, null=True),
        ),
    ]
