# Generated by Django 2.2 on 2020-02-28 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0003_user_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='action_phase',
            field=models.IntegerField(default=0),
        ),
    ]