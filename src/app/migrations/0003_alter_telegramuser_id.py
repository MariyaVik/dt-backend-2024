# Generated by Django 5.0.1 on 2024-02-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_telegramuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
