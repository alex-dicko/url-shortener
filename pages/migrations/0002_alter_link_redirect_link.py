# Generated by Django 4.2 on 2024-08-09 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='redirect_link',
            field=models.URLField(),
        ),
    ]
