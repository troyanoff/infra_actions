from django.http import HttpResponse


def index(request):
    value = 1234 * 4321 / 54321
    return HttpResponse(f'У меня получилось! {value}')


def second_page(request):
    return HttpResponse('А это вторая страница')
