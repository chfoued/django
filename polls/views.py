from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Operation, OperationForm
from django.utils import timezone 


# Create your views here.

def operation(request):
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            produit = form.cleaned_data['produit']
            poids = form.cleaned_data['poids']
            nbr_box = form.cleaned_data['nbr_box']
            client = form.cleaned_data['client']

            new_operation = Operation(produit= produit, date= timezone.now() , poids= poids, nbr_box= nbr_box, client= client)
            new_operation.save()

            return HttpResponse('/deatil/')


    else:
        form = OperationForm
    return render(request, 'polls/operation.html', {'form': form})

def detail(request):
    operation = Operation.objects.all()

    return render(request, 'polls/detail.html', {
    'operation': operation,
})
    
