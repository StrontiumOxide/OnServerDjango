from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from faker import Faker

# Create your views here.
def main_page(request: HttpRequest) -> HttpResponse:
    """Функция для отображения главной страницы сайта"""

    faker = Faker('ru_RU')
    count = request.GET.get('count', 2)
    list_name = [[order+1, faker.name(), faker.job(), faker.phone_number()] for order in range(int(count))]
    context = {'list_people': list_name}

    return render(
        request=request,
        template_name='main_page.html',
        context=context
    )
