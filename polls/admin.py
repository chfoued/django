from django.contrib import admin

# Register your models here.

from .models import Produit, Operation

admin.site.register(Produit)
admin.site.register(Operation)
