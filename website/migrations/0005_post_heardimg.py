# Generated by Django 3.0.3 on 2021-01-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20210102_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='heardImg',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
