from django.conf.urls import url
from .views import ListSucursales
from .views import DetailSucursal

urlpatterns = [
	url(r'^$', ListSucursales.as_view()),
	url(r'^(?P<pk>[0-9]+)/$',DetailSucursal.as_view())
]