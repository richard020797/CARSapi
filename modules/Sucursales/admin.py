from django.contrib import admin
from .models import Sucursal

class SucursalAdmin(admin.ModelAdmin):
	pass

admin.site.register(Sucursal,SucursalAdmin)