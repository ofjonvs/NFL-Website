# Generated by Django 4.1.4 on 2022-12-12 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_prospect_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospect',
            name='name_link',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]