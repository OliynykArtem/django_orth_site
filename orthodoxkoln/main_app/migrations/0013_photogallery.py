# Generated by Django 4.2.2 on 2023-07-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_calendar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photogallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотогалерея',
            },
        ),
    ]