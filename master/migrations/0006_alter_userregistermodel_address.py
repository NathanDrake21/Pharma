# Generated by Django 3.2.9 on 2021-11-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0005_alter_userregistermodel_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistermodel',
            name='address',
            field=models.TextField(max_length=80),
        ),
    ]
