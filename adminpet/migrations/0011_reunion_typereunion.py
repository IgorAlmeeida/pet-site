# Generated by Django 3.0.3 on 2020-12-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpet', '0010_auto_20201226_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='reunion',
            name='typeReunion',
            field=models.CharField(choices=[('Ordinária', 'Ordinária'), ('Extraórdinária', 'Extraórdinária')], default='Ordinária', max_length=20),
        ),
    ]
