# Generated by Django 2.2.5 on 2020-04-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmdr',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
