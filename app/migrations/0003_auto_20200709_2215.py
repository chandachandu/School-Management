# Generated by Django 3.0.6 on 2020-07-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_adminmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmodel',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
