# Generated by Django 2.2 on 2020-02-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0002_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='admin',
            field=models.IntegerField(default=0),
        ),
    ]
