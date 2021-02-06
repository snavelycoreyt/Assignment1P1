from django.db import models


class Store(models.Model):
    store_brand = models.CharField(max_length=200)
    store_addr = models.CharField(max_length=200)
    store_category = models.CharField(max_length=200)

    def __str__(self):
        return self.store_addr


class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    inventory_name = models.CharField(max_length=200)
    inventory_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.inventory_name

