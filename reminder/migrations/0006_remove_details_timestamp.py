# Generated by Django 3.0.3 on 2020-10-26 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0005_auto_20201026_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='timestamp',
        ),
    ]