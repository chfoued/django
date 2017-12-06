from django.contrib import admin

from .models import Question, Choice, Produit, Operation

class OperationAdmin(admin.ModelAdmin):
	list_display = ["produit", "date", "client", "poids", "nbr_cartons"]

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Produit)
admin.site.register(Operation, OperationAdmin)
# Register your models here.
