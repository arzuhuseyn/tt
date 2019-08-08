# Generated by Django 2.2.4 on 2019-08-07 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=600)),
                ('header', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Əlaqə forması',
                'verbose_name_plural': 'Əlaqə formaları',
            },
        ),
    ]