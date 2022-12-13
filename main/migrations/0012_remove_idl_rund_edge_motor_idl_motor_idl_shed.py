# Generated by Django 4.1.4 on 2022-12-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_shed_idl_rund'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idl',
            name='rund',
        ),
        migrations.AddField(
            model_name='edge',
            name='motor',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idl',
            name='motor',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idl',
            name='shed',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
            preserve_default=False,
        ),
    ]