from django.shortcuts import get_object_or_404, render
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

def main(request):
    return render(request, 'main_app/main.html', {'all_publication': all_publication})

def publication(request):
    return render(request, 'main_app/publication.html')


def bishop(request):
    return render(request, 'main_app/bishop.html')


all_parish = Parish.objects.all()

def parishes(request):
    return render(request, 'main_app/parishes.html', {'all_parish': all_parish})


def parish(request, parishid):
    return render(request, 'main_app/parish.html')


clergymans = Clergyman.objects.all()

def clergy(request):
    return render(request, 'main_app/clergy.html', {'clergymans': clergymans})

def clergyman(request, clergymanid):
    return render(request, 'main_app/clergyman.html')
    

def photogallery(request):
    return render(request, 'main_app/photogallery.html')


def contacts(request):
    return render(request, 'main_app/contacts.html')
