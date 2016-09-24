from django.conf.urls import url
from .views import ListMarcas
from .views import DetailMarca

urlpatterns = [
	url(r'^$', ListMarcas.as_view()),
	url(r'^(?P<pk>[0-9]+)/$',DetailMarca.as_view())
]