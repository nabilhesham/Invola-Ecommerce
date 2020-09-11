from django.db import models


class CoffeeMachine(models.Model):
    product_name = models.CharField(max_length=256)
    product_type_choices = (
        ("COFFEE_MACHINE_LARGE", "COFFEE MACHINE LARGE"),
        ("COFFEE_MACHINE_SMALL", "COFFEE MACHINE SMALL"),
        ("ESPRESSO_MACHINE", "ESPRESSO MACHINE"),
    )
    product_type = models.CharField(choices=product_type_choices, max_length=100)

    model_type_choices = (
        ("base_model", "Base Model"),
        ("premium_model", "Premium Model"),
        ("deluxe_model", "Deluxe Model"),
    )
    model_type = models.CharField(choices=model_type_choices, max_length=100)

    water_line_compatible = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name


class CoffeePod(models.Model):
    product_name = models.CharField(max_length=256)

    product_type_choices = (
        ("COFFEE_POD_LARGE", "COFFEE POD LARGE"),
        ("COFFEE_POD_SMALL", "COFFEE POD SMALL"),
        ("ESPRESSO_POD", "ESPRESSO POD"),
    )
    product_type = models.CharField(choices=product_type_choices, max_length=100)

    coffee_flavor_choices = (
        ("COFFEE_FLAVOR_VANILLA", "VANILLA"),
        ("COFFEE_FLAVOR_CARAMEL", "CARAMEL"),
        ("COFFEE_FLAVOR_PSL", "PSL"),
        ("COFFEE_FLAVOR_MOCHA", "MOCHA"),
        ("COFFEE_FLAVOR_HAZELNUT", "HAZELNUT"),
    )
    coffee_flavor = models.CharField(choices=coffee_flavor_choices, max_length=100)

    pack_size_choices = (
        (12, "1 dozen"),
        (36, "3 dozen"),
        (60, "5 dozen"),
        (84, "7 dozen"),
    )
    pack_size = models.PositiveIntegerField(choices=pack_size_choices)

    def __str__(self):
        return self.product_name
