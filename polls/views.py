from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect
from django.utils import timezone

from .models import Choice, Question, Operation, Produit, ProduitForm, OperationForm 

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question, 
			'error_message' : "you didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question_id)))

def operation(request):
	operation = Operation.objects.order_by('-date')[:5]
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



	return render(request, 'polls/operation.html', {
		'operation' : operation,
		'form' : form_class,
		})

def etat_produit(request, produit_id):
	produit = get_object_or_404(Produit, pk= produit_id)
	context = {
		'produit' : produit,
	}
	return render(request, 'polls/etat.html', context)

