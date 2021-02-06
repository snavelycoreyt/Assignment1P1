from django.contrib import admin

from .models import Store
from .models import Inventory

admin.site.register(Store)
admin.site.register(Inventory)