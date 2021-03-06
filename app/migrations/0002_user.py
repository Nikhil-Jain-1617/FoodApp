# Generated by Django 3.2.6 on 2021-08-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=40)),
                ('user_contact', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=30)),
                ('user_address', models.CharField(max_length=100)),
                ('item_name', models.CharField(default=None, max_length=50)),
                ('restaurant_name', models.CharField(default=None, max_length=50)),
            ],
        ),
    ]
