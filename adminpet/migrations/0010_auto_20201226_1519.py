# Generated by Django 3.0.3 on 2020-12-26 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpet', '0009_auto_20201226_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='reunion',
            name='ata',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reunion',
            name='dateReunion',
            field=models.DateField(default='1997-10-10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reunion',
            name='present',
            field=models.ManyToManyField(to='adminpet.Profile'),
        ),
        migrations.AddField(
            model_name='reunion',
            name='title',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
