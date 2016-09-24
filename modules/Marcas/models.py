from django.db import models

class Marca(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	trustScore = models.DecimalField(max_digits=3, decimal_places=1)
	country = models.CharField(max_length=20)
	
	def __str__(self):
		return 'Marca: ' + self.name