# Generated by Django 3.2.6 on 2021-09-18 03:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0014_remove_restaurant_max_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.uuid4, max_length=255)),
                ('door', models.CharField(blank=True, max_length=200, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kitchen', to='restaurants.restaurant')),
            ],
        ),
    ]
