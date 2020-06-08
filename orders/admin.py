from django.contrib import admin
from orders.models import PizzaSize, Pizza, PizzaTopping, Subs, SubsTopping, Pasta, Salad, DinnerPlatters

# Register your models here.

admin.site.register(PizzaSize)
admin.site.register(Pizza)
admin.site.register(PizzaTopping)
admin.site.register(Subs)
admin.site.register(SubsTopping)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatters)