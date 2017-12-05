from django.db import models
from django.forms import ModelForm

# Create your models here.

class Produit(models.Model):

    name = models.CharField(max_length=200)
    poids = models.FloatField(default=0)
    nbr_box = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Operation(models.Model):

    produit = models.ForeignKey(Produit)
    date = models.DateTimeField() 
    poids = models.FloatField(default=0)
    nbr_box = models.IntegerField(default=0)
    client = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        old_produit = Produit.objects.get(pk=self.produit.pk)
        old_produit.poids -= self.poids
        old_produit.nbr_box -= self.nbr_box
        old_produit.save()
        super(Operation, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        old_produit = Produit.objects.get(pk=self.produit.pk)
        old_produit.poids -= self.poids
        old_produit.nbr_box -= self.nbr_box
        old_produit.save()
        super(Operation, self).delete(*args, **kwargs)


class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = ['produit', 'poids', 'nbr_box', 'client']