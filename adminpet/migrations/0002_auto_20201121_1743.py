# Generated by Django 3.0.3 on 2020-11-21 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='typeUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminpet.TypeUser'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='adminpet.Status'),
        ),
    ]
