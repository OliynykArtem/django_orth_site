from django.shortcuts import get_object_or_404, render


def main(request):
    return render(request, 'main_app/main.html')


def bishop(request):
    return render(request, 'main_app/bishop.html')


def parishes(request):
    return render(request, 'main_app/parishes.html')


def parish(request, parishid):
    return render(request, 'main_app/parish.html')


def clergy(request):
    return render(request, 'main_app/clergy.html')


def photogallery(request):
    return render(request, 'main_app/photogallery.html')


def contacts(request):
    return render(request, 'main_app/contacts.html')
