# Generated by Django 2.0.4 on 2018-05-03 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internal', '0006_uploadrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadrecord',
            name='user',
        ),
    ]
