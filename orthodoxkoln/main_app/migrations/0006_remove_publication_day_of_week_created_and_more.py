# Generated by Django 4.2.2 on 2023-07-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_parish_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='day_of_week_created',
        ),
        migrations.AlterField(
            model_name='clergyman',
            name='job_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Духовна посада'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='publicationvideo',
            name='video',
            field=models.FileField(max_length=255, upload_to='media/', verbose_name='Відео'),
        ),
    ]
