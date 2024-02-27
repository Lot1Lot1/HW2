from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    # получите список авто
    context = {'cars': Car.objects.all}
    template_name = 'main/list.html'
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    try:
        # получите авто, если же его нет, выбросьте ошибку 404
        context = {'car':Car.objects.get(id=car_id)}
        template_name = 'main/details.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')

def sales_by_car(request, car_id):
    try:
        car1 = Car.objects.get(id=car_id)
        context = {'car': car1, 'sales': Sale.objects.filter(car=car1)}
        template_name = 'main/sales.html'
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
