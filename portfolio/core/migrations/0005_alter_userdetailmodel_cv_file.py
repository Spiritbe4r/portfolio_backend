# Generated by Django 4.1.1 on 2023-01-04 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_userdetailmodel_cv_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetailmodel',
            name='cv_file',
            field=models.FileField(blank=True, upload_to='raw'),
        ),
    ]
