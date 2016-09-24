from django.contrib import admin
from .models import Aseguradora

class AseguradoraAdmin(admin.ModelAdmin):
	pass

admin.site.register(Aseguradora,AseguradoraAdmin)

