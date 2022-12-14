# Generated by Django 4.1.4 on 2022-12-12 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_gradedescriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('school', models.CharField(max_length=30)),
                ('grade', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.AddField(
            model_name='quarterback',
            name='prospect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.prospect'),
        ),
    ]
