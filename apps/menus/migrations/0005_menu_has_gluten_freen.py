# Generated by Django 3.2.6 on 2021-09-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_remove_menu_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='has_gluten_freen',
            field=models.BooleanField(default=False),
        ),
    ]