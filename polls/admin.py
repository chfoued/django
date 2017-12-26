from django.contrib import admin

from .models import Produit, Operation, Client

class OperationAdmin(admin.ModelAdmin):
	list_display = ["produit", "date", "client", "poids", "nbr_cartons"]

admin.site.register(Produit)
admin.site.register(Client)
admin.site.register(Operation, OperationAdmin)
# Register your models here.
