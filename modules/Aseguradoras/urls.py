from django.conf.urls import url
from .views import ListAseguradoras
from .views import DetailAseguradora

urlpatterns = [
	url(r'^$', ListAseguradoras.as_view()),
	url(r'^(?P<pk>[0-9]+)/$',DetailAseguradora.as_view())
]