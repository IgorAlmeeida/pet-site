# Generated by Django 3.0.3 on 2021-01-02 13:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpet', '0012_auto_20210102_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='reference',
            field=ckeditor.fields.RichTextField(),
        ),
    ]