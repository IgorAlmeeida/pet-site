# Generated by Django 3.0.3 on 2020-12-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpet', '0006_profile_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='typeUser',
            field=models.CharField(choices=[('T', 'Tutor'), ('P', 'Petiano')], max_length=2),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('A', 'Ativo'), ('I', 'Inativo')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.DeleteModel(
            name='TypeUser',
        ),
    ]
