# Generated by Django 3.0.3 on 2020-10-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_auto_20201025_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
    ]
