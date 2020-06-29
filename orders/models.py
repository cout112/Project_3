from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PizzaStyle (models.Model):
	style = models.CharField(max_length=64)

	def  __str__(self):
		return self.style

class PizzaSize (models.Model):
	size = models.CharField(max_length=64)

	def  __str__(self):
		return self.size

class PizzaToppingsClass(models.Model):
	classification = models.CharField(max_length=64)

	def __str__(self):
		return self.classification

class Pizza (models.Model):
	style = models.ForeignKey(PizzaStyle, on_delete=models.CASCADE)
	size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
	price0= models.DecimalField(max_digits=5, decimal_places=2, null=True)
	price1= models.DecimalField(max_digits=5, decimal_places=2, null=True)
	price2= models.DecimalField(max_digits=5, decimal_places=2, null=True)
	price3= models.DecimalField(max_digits=5, decimal_places=2, null=True)
	price4= models.DecimalField(max_digits=5, decimal_places=2, null=True)


	def __str__(self):
		return f"Pizza {self.style} {self.size}: {self.price0},{self.price2},{self.price3},{self.price4}"


class PizzaTopping(models.Model):
	name = models.CharField(max_length=64)

	def __str__ (self):
		return f"{self.name}"

class Subs (models.Model):
	name = models.CharField(max_length=64)
	small = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	large = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

	def __str__(self):
		return f"{self.name}, small:{self.small},large:{self.large}"

class SubsTopping (models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name}:{self.price}"

class Pasta(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name}:{self.price}"

class Salad (models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name}:{self.price}"

class DinnerPlatters (models.Model):
	name = models.CharField(max_length=64)
	small = models.DecimalField(max_digits=5, decimal_places=2)
	large = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name}: Small {self.small}, Large {self.large}"

class Address(models.Model):
	country = models.CharField(max_length=64)
	state = models.CharField (max_length=64)
	city = models.CharField(max_length=64)
	street = models.CharField(max_length=128)
	number = models.CharField(max_length=10)
	apartment = models.CharField(max_length=20, null=True, blank=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')

	def __str__(self):
		return f"{self.street} {self.number}, {self.apartment}, {self.city}, {self.country}"


# class State(models.Model):
#  	state=models.CharField(max_length=64)

#  	def __str__(self):
#  		return f"{self.state}"


class Orders(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	items = models.TextField()
	total = models.DecimalField(max_digits=5, decimal_places=2)
	address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='orders')
	#state = models.ForeignKey(State, on_delete=models.SET_DEFAULT, default=0, blank=True, related_name="orders")

	def __str__(self):
		return f"{self.user}: {self.items} to {self.address} for  {self.total}: Status = {state}"












