from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^operation/$', views.operation, name='operations'),
	url(r'^produit/(?P<produit_id>[0-9]+)/$', views.etat_produit, name='etat'),
	url(r'^stock/$', views.stock, name='stock'),
]