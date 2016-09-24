from django.db import models

class Aseguradora(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=25)
	country = models.CharField(max_length=20)
	costRateTop = models.DecimalField(max_digits=10, decimal_places=2)
	costRateBottom = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return 'Aseguradora: ' + self.name
