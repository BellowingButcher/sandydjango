from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pizza
from pprint import pprint


def get_all_pizzas(request):
    if request.method == 'GET':
        pizzas = list(Pizza.objects.values())
        pprint(pizzas)
        # return HttpResponse('Orders')
        return JsonResponse({'pizzas': pizzas})
#     data = list(SomeModel.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
#     return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})
    else:
        print('It was not a GET request')
        return HttpResponse("else time.")

def get_orders_by_person(request, name):
    pizzas = list(Pizza.objects.values())
    pprint(pizzas)
    return JsonResponse(pizzas)

def all_orders_by_id(request, id):
    print(id)
    return HttpResponse(f"The order number is {id}")