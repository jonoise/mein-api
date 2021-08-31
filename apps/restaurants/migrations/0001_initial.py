# Generated by Django 3.2.6 on 2021-08-31 07:43

import apps.restaurants.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_account_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type_of', models.CharField(max_length=20)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=apps.restaurants.models.restaurante_logo_path)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='users.account')),
            ],
        ),
    ]
