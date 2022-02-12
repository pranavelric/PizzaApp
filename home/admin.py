from django.contrib import admin
from .models import Order, Pizza
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pizza','users','order_id','amount','status','date']


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name','price','image']



