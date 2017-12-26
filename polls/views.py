from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect
from django.utils import timezone

from .models import  Operation, Produit, ProduitForm, OperationForm 

from reportlab.pdfgen import canvas
from io import BytesIO


#############################################################
def operation(request):
	operation = Operation.objects.order_by('-date')[:20]
	form_class = OperationForm
	if request.method == 'POST':
		formset = form_class(request.POST, request.FILES)
		if formset.is_valid():
			produit = formset.cleaned_data['produit']
			poids = formset.cleaned_data['poids']
			nbr_cartons = formset.cleaned_data['nbr_cartons']
			client = formset.cleaned_data['client']
			operation = Operation(produit=produit, poids=poids, nbr_cartons=nbr_cartons, client=client, date=timezone.now())
			operation.save()
			return redirect('../produit/' + str(produit.pk))

	return render(request, 'polls/operation2.html', {
		'operation' : operation,
		'form' : form_class,
		})
#############################################################
def export_pdf(request, produit_id):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachement; filename="test.pdf"'
	produit = get_object_or_404(Produit, pk= produit_id)
	context = {
		'produit' : produit,
	}
	buffer = BytesIO()
	p = canvas.Canvas(buffer)

	p.setFont("Helvetica", 20)

	p.drawString(250, 800, produit.name)
	p.setFont("Helvetica", 14)
	p.drawString(0, 750, "poids: " ) 
	p.setFont("Helvetica", 12)
	p.drawString(200, 750, str(produit.Poids))

	p.setFont("Helvetica", 14)
	p.drawString(0, 730, "Nbr cartons: " ) 
	p.setFont("Helvetica", 12)
	p.drawString(200, 730, str(produit.nbr_cartons))

	p.showPage()
	p.save()

	pdf = buffer.getvalue()
	buffer.close()
	response.write(pdf)



	return response
#############################################################
def etat_produit (request, produit_id):
	produit = get_object_or_404(Produit, pk=produit_id)
	operation = Operation.objects.all().filter(produit=produit)
	context ={
		'produit': produit,
		'operation': operation,
	}
	return render(request, 'polls/etat.html', context)
#############################################################
def stock(request):
	produit = Produit.objects.order_by('-name')

	return render(request, 'polls/stock.html', {
		'produit' : produit,
		})
#############################################################

