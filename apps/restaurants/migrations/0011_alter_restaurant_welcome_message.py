# Generated by Django 3.2.6 on 2021-09-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_restaurant_max_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='welcome_message',
            field=models.CharField(blank=True, max_length=145, null=True),
        ),
    ]