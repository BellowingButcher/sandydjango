from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the pizza index.")

def cheese(request):
    return HttpResponse("Hello, world. You're at the cheese pizza index.")

def pepperoni(request):
    return HttpResponse("Hello, world. You're at the pepperoni pizza index.")