from django.contrib import admin
from .models import Auto

class AutoAdmin(admin.ModelAdmin):
	pass

admin.site.register(Auto,AutoAdmin)