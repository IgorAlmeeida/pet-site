# Generated by Django 3.0.3 on 2020-11-26 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpet', '0003_auto_20201125_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='realizationDate',
            field=models.DateTimeField(),
        ),
    ]
