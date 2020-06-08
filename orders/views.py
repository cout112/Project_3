from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from orders.models import PizzaSize, Pizza, PizzaTopping, Subs, SubsTopping, Pasta, Salad, DinnerPlatters
from django.urls import reverse



def index(request):
	context = {
		"pizzas":Pizza.objects.all(),
		"toppings":PizzaTopping.objects.all(),
		"subs":Subs.objects.all(),
		"substoppings":SubsTopping.objects.all(),
		"salads":Salad.objects.all(),
		"pastas":Pasta.objects.all(),
		"dinnerplatters":DinnerPlatters.objects.all()
	}
	return render(request, "index.html", context)
