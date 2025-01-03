# Generated by Django 4.2.1 on 2023-06-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lieu', models.CharField(max_length=100)),
                ('surface', models.FloatField(blank=True)),
                ('culture', models.CharField(max_length=100)),
                ('renseignements', models.CharField(max_length=100)),
                ('date_mise', models.DateField(blank=True, null=True)),
                ('jachere', models.BooleanField(blank=True, null=True)),
            ],
        ),
    ]
