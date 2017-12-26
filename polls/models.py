import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.


########################################################################

class Produit(models.Model):

	name = models.CharField(max_length=200)
	Poids = models.FloatField(default=0)
	nbr_cartons = models.IntegerField(default=0)
	def __str__(self):
		return self.name

########################################################################

class Client(models.Model):

	name = models.CharField(max_length=200)
	credit = models.IntegerField()

	def __str__(self):
		return self.name

########################################################################

class Operation(models.Model):

	produit = models.ForeignKey(Produit)
	poids = models.FloatField(default=0)
	nbr_cartons = models.IntegerField(default=0)
	client = models.ForeignKey(Client)
	date = models.DateField("Date de l'opération")

	def save(self, *args, **kwargs):
		new_produit = Produit.objects.get(pk= self.produit.pk)
		new_client = Client.objects.get(pk=self.client.pk)
		new_client.credit += self.poids
		new_produit.Poids -= self.poids
		new_produit.nbr_cartons -= self.nbr_cartons
		new_client.save()
		new_produit.save()
		super(Operation, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		operation = Operation.objects.get(pk= self.pk)
		produit = Produit.objects.get(pk= operation.produit.pk)
		produit.Poids += operation.poids
		produit.nbr_cartons += operation.nbr_cartons 
		produit.save()
		super(Operation, self).delete(*args, **kwargs)

########################################################################





class ProduitForm(ModelForm):
	class Meta:
		model =Produit
		fields = ['name', 'Poids', 'nbr_cartons']


class OperationForm(ModelForm):
	class Meta:
		model = Operation
		fields = ['produit', 'poids', 'nbr_cartons', 'client']


