# Generated by Django 3.2.6 on 2021-09-03 06:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('table_instances', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tableinstance',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='tableinstance',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]