# Generated by Django 4.2.1 on 2023-07-18 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_favourite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='History',
        ),
    ]
