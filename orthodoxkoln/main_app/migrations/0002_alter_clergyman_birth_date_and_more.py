# Generated by Django 4.2.2 on 2023-06-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clergyman',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Дата народження'),
        ),
        migrations.AlterField(
            model_name='clergyman',
            name='deacon_ordination_date',
            field=models.DateField(null=True, verbose_name='Дияконська хіротонія'),
        ),
        migrations.AlterField(
            model_name='clergyman',
            name='image',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='clergyman',
            name='job_title',
            field=models.CharField(max_length=200, null=True, verbose_name='Духовна посада'),
        ),
        migrations.AlterField(
            model_name='clergyman',
            name='priest_ordination_date',
            field=models.DateField(null=True, verbose_name='Ієрейська хіротонія'),
        ),
        migrations.AlterField(
            model_name='clergyman',
            name='secular_education',
            field=models.TextField(null=True, verbose_name='Світська освіта'),
        ),
        migrations.AlterField(
            model_name='clergyman',
            name='spiritual_education',
            field=models.TextField(null=True, verbose_name='Духовна освіта'),
        ),
        migrations.AlterField(
            model_name='parish',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Адреса'),
        ),
        migrations.AlterField(
            model_name='parish',
            name='date_of_establishment',
            field=models.DateField(null=True, verbose_name='Дата заснування'),
        ),
        migrations.AlterField(
            model_name='parish',
            name='history',
            field=models.TextField(null=True, verbose_name='Історія'),
        ),
        migrations.AlterField(
            model_name='parish',
            name='main_image',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Головне фото'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='main_image',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Головне фото'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='text',
            field=models.TextField(null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='publicationvideo',
            name='video',
            field=models.FileField(max_length=200, upload_to='media/', verbose_name='Відео'),
        ),
    ]