# Generated by Django 4.1 on 2022-11-14 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_bookins_options_bookins_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookins',
            name='test',
        ),
    ]