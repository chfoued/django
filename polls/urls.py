from django.conf.urls import url
from polls.views import operation, detail


urlpatterns=[
    url(r'^operation/', operation),
    url(r'^detail/', detail ),

]