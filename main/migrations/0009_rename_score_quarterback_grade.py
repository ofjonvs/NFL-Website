# Generated by Django 4.1.4 on 2022-12-12 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_quarterback_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quarterback',
            old_name='score',
            new_name='grade',
        ),
    ]
