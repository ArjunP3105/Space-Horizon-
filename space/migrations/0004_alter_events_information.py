# Generated by Django 5.1 on 2024-11-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0003_alter_events_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='information',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
