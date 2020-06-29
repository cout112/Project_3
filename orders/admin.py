from django.contrib import admin
from orders.models import PizzaSize, PizzaStyle, PizzaToppingsClass, Pizza, PizzaTopping, Subs, SubsTopping, Pasta, Salad, DinnerPlatters, Address, Orders#, State

# Register your models here.

admin.site.register(PizzaStyle)
admin.site.register(PizzaSize)
admin.site.register(PizzaToppingsClass)
admin.site.register(Pizza)
admin.site.register(PizzaTopping)
admin.site.register(Subs)
admin.site.register(SubsTopping)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatters)
admin.site.register(Address)
admin.site.register(Orders)
#admin.site.register(State)