from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from orders.models import PizzaSize, Pizza, PizzaTopping, Subs, SubsTopping, Pasta, Salad, DinnerPlatters, Address
from django.urls import reverse


context = {
		"pizzas":Pizza.objects.all(),
		"toppings":PizzaTopping.objects.all(),
		"subs":Subs.objects.all(),
		"substoppings":SubsTopping.objects.all(),
		"salads":Salad.objects.all(),
		"pastas":Pasta.objects.all(),
		"dinnerplatters":DinnerPlatters.objects.all(),
		"address":Address.objects.all(),
	}


def index(request):
	
	
	#user = authenticate(request)
	if not request.user.is_authenticated:
		print ("Not authenticated")
		return render(request, "index.html", context)
	print ("Authenticated")
	return render(request, "orders.html", context)
	

def login_view(request):
	if not request.user.is_authenticated:
		return render(request, "login.html")
	return render (request, "userpage.html", context)

def login_authenticate(request):
	user = None
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		print (f"\nlogin request for username:{username}, with password:{password}\n")
		user = authenticate(request, username=username, password=password)
		print (f"user authentication is {user}")
	if user is not None:
		login(request, user)	
		return render(request, "orders.html", context)
	else:
		return render(request, "login.html", {"message": "Invalid credentials."})
	

def signup(request):
	#user = None
	if request.method != 'POST':
		return render(request, "login.html")
	if request.POST['password1'] != request.POST['password2']:
		return render(request, "login.html", {"message2":"Password doesn't match"})
	email = request.POST['email']
	check_email = User.objects.filter(email=email)
	if  check_email:
		return render(request, "login.html", {"message2":"Email already exists"})
	username = request.POST['username']
	check_username = User.objects.filter(username = username)
	if check_username:
		return render(request, "login.html", {"message2":"Username already exists"})
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']					
	password = request.POST['password1']
	User.objects.create_user(username, email=email, password=password)
	user= User.objects.get(username=username)
	user.first_name=first_name
	user.last_name=last_name
	user.save()
	
	return render(request, "orders.html", context)
	
	




def logout_view(request):
	logout(request)
	
	return render(request, "index.html", context)

def add_address(request):
	context = {
		"orders":"",
		"address":Address.objects.filter(user=username),
	}
	if request.method !=  'POST':
		return render(request, "userpage.html", context)
	return 'added address'










