from django.contrib import admin
from .models import OilProduct, Storage, Transaction

admin.site.register(OilProduct)
admin.site.register(Storage)
admin.site.register(Transaction)
