# Generated by Django 5.1 on 2024-11-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0002_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='information',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
