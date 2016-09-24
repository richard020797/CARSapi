from django.db import models
from modules.Marcas.models import Marca


class Sucursal(models.Model):
	id = models.AutoField(primary_key=True)
	idMarca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='stores')
	direccion = models.CharField(max_length=50)
	
	def __str__(self):
		return 'Dirección Sucursal: ' + self.direccion
