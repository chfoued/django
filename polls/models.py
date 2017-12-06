import datetime

from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.

class Question(models.Model):

	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):

	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text


class Produit(models.Model):

	name = models.CharField(max_length=200)
	Poids = models.FloatField(default=0)
	nbr_cartons = models.IntegerField(default=0)
	def __str__(self):
		return self.name



class Operation(models.Model):

	produit = models.ForeignKey(Produit)
	poids = models.FloatField(default=0)
	nbr_cartons = models.IntegerField(default=0)
	client = models.CharField(max_length=200)
	date = models.DateField("Date de l'opération")

	def save(self, *args, **kwargs):
		new_produit = Produit.objects.get(pk= self.produit.pk)

		new_produit.Poids -= self.poids
		new_produit.nbr_cartons -= self.nbr_cartons
		new_produit.save()
		super(Operation, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		operation = Operation.objects.get(pk= self.pk)
		produit = Produit.objects.get(pk= operation.produit.pk)
		produit.Poids += operation.poids
		produit.nbr_cartons += operation.nbr_cartons 
		produit.save()
		super(Operation, self).delete(*args, **kwargs)


class Client(models.Model):

	name = models.CharField(max_length=200)
	credit = models.IntegerField()


class ProduitForm(ModelForm):
	class Meta:
		model =Produit
		fields = ['name', 'Poids', 'nbr_cartons']


class OperationForm(ModelForm):
	class Meta:
		model = Operation
		fields = ['produit', 'poids', 'nbr_cartons', 'client']


