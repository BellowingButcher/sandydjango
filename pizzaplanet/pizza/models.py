from django.db import models
class Pizza(models.Model):
    ordered_by = models.CharField(default='', max_length=30)
    address_ordered_from = models.CharField(default='', max_length=99)
    type_of_pizza = models.CharField(default='', max_length=99)