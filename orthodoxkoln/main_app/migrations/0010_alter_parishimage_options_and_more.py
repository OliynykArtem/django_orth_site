# Generated by Django 4.2.2 on 2023-07-11 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_parishimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parishimage',
            options={'verbose_name': 'Фото парафії', 'verbose_name_plural': 'Фото парафій'},
        ),
        migrations.AlterModelOptions(
            name='publicationimage',
            options={'verbose_name': 'Фото публікації', 'verbose_name_plural': 'Фото публікацій'},
        ),
        migrations.AlterField(
            model_name='parishimage',
            name='parish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.parish', verbose_name='Парафія'),
        ),
    ]
