# Generated by Django 5.1.4 on 2025-05-07 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_create_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_no',
            field=models.IntegerField(unique=True),
        ),
    ]
