from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from main_app.models import *
import logging

# Отримання екземпляра логгера
logger = logging.getLogger(__name__)

# Налаштування рівня журналювання
logger.setLevel(logging.DEBUG)

# Налаштування обробника для виводу в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Налаштування формату повідомлень
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Додавання обробника до логгера
logger.addHandler(console_handler)



all_publication = Publication.objects.all()
# paginator = Paginator(all_publication, 3)
# logger.debug(paginator.count)
# logger.debug(paginator.num_pages)
# logger.debug(paginator.page_range)
# p = paginator.page(1)
# publications_by_page_number = p.object_list
# logger.debug(p.object_list)
# logger.debug(all_publication)

def main(request):
    paginator = Paginator(all_publication, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main_app/main.html', {'page_obj': page_obj})

def publication(request, publicationid):
    publication_from_db = Publication.objects.get(pk=publicationid)
    publication_images_from_db = publication_from_db.publicationimage_set.all()
    return render(request, 'main_app/publication.html', {'publication_from_db': publication_from_db, 'publication_images_from_db': publication_images_from_db})


def bishop(request):
    return render(request, 'main_app/bishop.html')


all_parish = Parish.objects.all()

def parishes(request):
    return render(request, 'main_app/parishes.html', {'all_parish': all_parish})


def parish(request, parishid):
    parish_from_db = Parish.objects.get(pk=parishid)
    parish_images_from_db = parish_from_db.parishimage_set.all()
    return render(request, 'main_app/parish.html', {'parish_from_db': parish_from_db, 'parish_images_from_db': parish_images_from_db})


clergymans = Clergyman.objects.all()

def clergy(request):
    return render(request, 'main_app/clergy.html', {'clergymans': clergymans})

def clergyman(request, clergymanid):
    clergyman_from_db = Clergyman.objects.get(pk=clergymanid)
    return render(request, 'main_app/clergyman.html', {'clergyman_from_db': clergyman_from_db})
    

def photogallery(request):
    return render(request, 'main_app/photogallery.html')


def contacts(request):
    return render(request, 'main_app/contacts.html')
