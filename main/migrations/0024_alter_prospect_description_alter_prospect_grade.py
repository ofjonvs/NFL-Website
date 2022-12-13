# Generated by Django 4.1.4 on 2022-12-13 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_prospect_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospect',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='prospect',
            name='grade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
