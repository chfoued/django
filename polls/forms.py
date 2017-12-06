from django import forms
from .models import Produit


class ProduitForm(forms.Form):
	name = forms.CharField(max_length=200)
	Poids = forms.FloatField()
	nbr_carton = forms.IntegerField()

class OperationForm(forms.Form):
	produit = forms.ModelChoiceField(queryset=Produit.objects.all())
	poids = forms.FloatField()
	nbr_carton = forms.IntegerField()
	client = forms.CharField(max_length=200)
	date = forms.DateField()






		