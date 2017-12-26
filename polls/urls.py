from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
	url(r'^operation/$', views.operation, name='operations'),
	url(r'^produit/(?P<produit_id>[0-9]+)/$', views.etat_produit, name='etat'),
	url(r'^stock/$', views.stock, name='stock'),
	url(r'^export/(?P<produit_id>[0-9]+)/$', views.export_pdf, name='pdf'),
]