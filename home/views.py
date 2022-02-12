import imp
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pizza =Pizza.objects.all()
        
        context["pizza"] = pizza 
        return context
    
    def get(self, request, *args, **kwargs) :
        orders = Order.objects.filter(users = request.user)
        context = self.get_context_data()
        context["orders"] = orders
        return super(TemplateView, self).render_to_response(context)
    
class OrderPizzaView(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get(self, request, *args, **kwargs) :
        id =kwargs.get('id')
        order = Order.objects.filter(order_id = id).first()
        context = self.get_context_data()
        if order is None:
            return HttpResponseRedirect("/")
        context["order"] = order
        return super(TemplateView, self).render_to_response(context)

@method_decorator(csrf_exempt, name='dispatch')
class OrderPizza(View):
    
    def post(self,request):
        user = request.user
        data= json.loads(request.body)
        try:
            pizza = Pizza.objects.get(id=data.get("id"))
            order= Order(users=user,pizza=pizza,amount=pizza.price)
            order.save()
            return JsonResponse({'message':'Success'})
        except Pizza.DoesNotExist:
            return JsonResponse({'error':'Something went wrong'})

    