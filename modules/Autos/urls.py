from django.conf.urls import url
from .views import ListAutos
from .views import DetailAuto

urlpatterns = [
	url(r'^$', ListAutos.as_view()),
	url(r'^(?P<pk>[0-9]+)/$',DetailAuto.as_view())
]