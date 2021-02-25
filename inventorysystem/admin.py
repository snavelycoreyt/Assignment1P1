from django.contrib import admin

from .models import Store
from .models import Inventory


class StoreList(admin.ModelAdmin):
    list_display = ('store_brand', 'store_addr', 'store_category')
    list_filter = ('store_brand', 'store_category')
    search_fields = ('store_brand',)
    ordering = ['store_brand']


class InventoryList(admin.ModelAdmin):
    list_display = ('inventory_name', 'inventory_amount')
    list_filter = ('inventory_name', 'inventory_amount')
    search_fields = ('inventory_name', 'store')
    ordering = ['inventory_name', 'store']


admin.site.register(Store)
admin.site.register(Inventory)
