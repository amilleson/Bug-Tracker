# Generated by Django 2.2 on 2020-06-04 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bug', '0005_ticket_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='vote',
        ),
    ]
