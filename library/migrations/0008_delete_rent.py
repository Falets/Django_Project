# Generated by Django 4.1 on 2022-11-15 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_bookins_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rent',
        ),
    ]
