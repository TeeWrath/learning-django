# Generated by Django 4.2.7 on 2024-01-04 18:56

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_des',
            field=tinymce.models.HTMLField(),
        ),
    ]