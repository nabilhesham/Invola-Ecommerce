from django.contrib import admin
from .models import CoffeePod, CoffeeMachine


@admin.register(CoffeePod)
class CoffeePod(admin.ModelAdmin):
    model = CoffeePod


@admin.register(CoffeeMachine)
class CoffeeMachine(admin.ModelAdmin):
    model = CoffeeMachine