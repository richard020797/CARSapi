
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/aseguradoras/', include('modules.Aseguradoras.urls', namespace="Aseguradoras")),
    url(r'^api/autos/', include('modules.Autos.urls', namespace="Autos")),
    url(r'^api/marcas/', include('modules.Marcas.urls', namespace="Marcas")),
    url(r'^api/sucursales/', include('modules.Sucursales.urls', namespace="Sucursales")),

    #RUTE FOR AUTHENTICATION

    url(r'^api-auth/', obtain_jwt_token),
]

