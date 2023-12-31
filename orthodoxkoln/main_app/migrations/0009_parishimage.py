# Generated by Django 4.2.2 on 2023-07-11 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_publication_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParishImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Фото')),
                ('parish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.parish')),
            ],
        ),
    ]
