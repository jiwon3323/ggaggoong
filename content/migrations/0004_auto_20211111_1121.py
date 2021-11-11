# Generated by Django 3.2.8 on 2021-11-11 02:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0003_contents_payed_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contents',
            name='payed_user',
        ),
        migrations.AddField(
            model_name='contents',
            name='payed_user',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
