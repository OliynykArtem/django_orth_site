# Generated by Django 4.2.2 on 2023-07-07 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_publication_day_of_week_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parish',
            name='name',
            field=models.TextField(max_length=255, verbose_name='Назва'),
        ),
    ]