from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pprint import pprint


def get_all_pizzas(request):
    if request.method == 'GET':
        print('It was a GET request')
        return HttpResponse("Hello, world. You're at the all orders index.")

    else:
        print('It was not a GET request')
        return HttpResponse("else time.")

def get_orders_by_person(request, name):
    print(name)
    return HttpResponse("Hello, world. You're at the orders by person index.")

def all_orders_by_id(request, id):
    print(id)
    return HttpResponse("Hello, world. You're at the orders by pizza type index.")