from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def ice_cream_list(request):
    return HttpResponse('Список мороженного')


def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженное номер {pk}')
