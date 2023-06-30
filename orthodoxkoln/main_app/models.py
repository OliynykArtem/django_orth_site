from django.db import models
from django.utils.translation import gettext_lazy as _

class Publication(models.Model):
    title = models.CharField(verbose_name="Заголовок", null=True, max_length=50)
    text = models.TextField(verbose_name="Текст", null=True)
    main_image = models.ImageField(verbose_name="Головне фото", null=True,
     upload_to="media/", height_field=None, width_field=None, max_length=None)
    date_created = models.DateField(verbose_name="Дата створення", auto_now=False, auto_now_add=True)

    DAY_OF_WEEK_CHOICES = (
        ('MONDAY', 'Понеділок'),
        ('TUESDAY', 'Вівторок'),
        ('WEDNESDAY', 'Середа'),
        ('THURSDAY', 'Четвер'),
        ('FRIDAY', "П'ятниця"),
        ('SATURDAY', 'Субота'),
        ('SUNDAY', 'Неділя'),
    )
    day_of_week_created = models.CharField(verbose_name="День створення", max_length=20, choices=DAY_OF_WEEK_CHOICES)

class PublicationImage(models.Model):
    publication = models.ForeignKey("Publication", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Фото", upload_to="media/", height_field=None, width_field=None, max_length=None)

class PublicationVideo(models.Model):
    publication = models.ForeignKey("Publication", on_delete=models.CASCADE)
    video = models.FileField(verbose_name="Відео", upload_to="media/", max_length=200)
    
class Clergyman(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=50)
    image = models.ImageField(verbose_name="Фото", null=True, upload_to="media/", height_field=None, width_field=None, max_length=None)
    job_title = models.CharField(verbose_name="Духовна посада", null=True, max_length=200)
    birth_date = models.DateField(verbose_name="Дата народження", null=True, auto_now=False, auto_now_add=False)
    deacon_ordination_date = models.DateField(verbose_name="Дияконська хіротонія", null=True, auto_now=False, auto_now_add=False)
    priest_ordination_date = models.DateField(verbose_name="Ієрейська хіротонія", null=True, auto_now=False, auto_now_add=False)
    secular_education = models.TextField(verbose_name="Світська освіта", null=True)
    spiritual_education = models.TextField(verbose_name="Духовна освіта", null=True)

class Parish(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=50)
    main_image = models.ImageField(verbose_name="Головне фото", null=True, upload_to="media/", height_field=None, width_field=None, max_length=None)
    address = models.CharField(verbose_name="Адреса", null=True, max_length=255)
    date_of_establishment = models.DateField(verbose_name="Дата заснування", null=True, auto_now=False, auto_now_add=False)
    history = models.TextField(verbose_name="Історія", null=True)

class Bishop(models.Model):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    image = models.ImageField(verbose_name="Фото", upload_to=None, height_field=None, width_field=None, max_length=None)
    birth_date = models.DateField(verbose_name="Дата народження", auto_now=False, auto_now_add=False)
    name_day = models.CharField(verbose_name="День тезоіменитства", max_length=20)
    tonsure_date = models.DateField(verbose_name="Дата постригу", auto_now=False, auto_now_add=False)
    deacon_ordination_date = models.DateField(verbose_name="Дата дияконської хіротонії", auto_now=False, auto_now_add=False)
    priest_ordination_date = models.DateField(verbose_name="Дата ієрейської хіротонії", auto_now=False, auto_now_add=False)
    bishop_ordination_date = models.DateField(verbose_name="Дата Архієрейської хіротонії", auto_now=False, auto_now_add=False)
    secular_education = models.TextField(verbose_name="Світська освіта")
    spiritual_education = models.TextField(verbose_name="Духовна освіта")
    biography = models.TextField(verbose_name="Біографія")


# class Meta:
#     verbose_name = _("Publication")
#     verbose_name_plural = _("Publications")

# def __str__(self):
#     return self.name

# def get_absolute_url(self):
#     return reverse("Publication_detail", kwargs={"pk": self.pk})