# Generated by Django 4.0 on 2021-12-14 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('master', '0009_addcartmodel_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffRegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=18)),
                ('address', models.CharField(max_length=80)),
                ('Profile_picture', models.ImageField(upload_to='idcard/')),
                ('status', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
