# Generated by Django 4.1.1 on 2023-01-04 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetailmodel',
            name='welcome_description',
            field=models.TextField(max_length=500),
        ),
    ]
