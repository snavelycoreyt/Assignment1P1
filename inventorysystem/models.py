from django.db import models
from django.utils import timezone

class Store(models.Model):
    store_brand = models.CharField(max_length=200)
    store_addr = models.CharField(max_length=200)
    store_category = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.store_addr


class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    inventory_name = models.CharField(max_length=200)
    inventory_amount = models.IntegerField(default=0)
    created_date = models.DateTimeField(
        default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.inventory_name

