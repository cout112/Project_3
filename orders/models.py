from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PizzaSize (models.Model):
	size = models.CharField(max_length=64)

	def  __str__(self):
		return self.size

class Pizza (models.Model):
	style = models.CharField(max_length=64)
	size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE)
	price0 = models.DecimalField(max_digits=5, decimal_places=2)
	price1 = models.DecimalField(max_digits=5, decimal_places=2)
	price2 = models.DecimalField(max_digits=5, decimal_places=2)
	price3 = models.DecimalField(max_digits=5, decimal_places=2)
	price4 = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"Pizza {self.style} {self.size}"


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
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')

	def __str__(self):
		return f"{Street} {number}, {apartment}, {city}, {state}"


















