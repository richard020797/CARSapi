from django.db import models
from modules.Marcas.models import Marca


class Auto(models.Model):

	id = models.AutoField(primary_key=True)
	brand = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, related_name='cars')
	model = models.CharField(max_length=20)
	year = models.IntegerField()
	ncapScore = models.CharField(max_length=8, choices=(('1','1 star'),('2','2 stars'),('3','3 stars'),('4','4 stars'),('5','5 stars')))
	airbags = models.IntegerField()
	noDoors = models.IntegerField()
	trunkCapacity = models.DecimalField(max_digits=6, decimal_places=2)
	kmPerChargeTank = models.DecimalField(max_digits=7, decimal_places=2)
	height = models.DecimalField(max_digits=8, decimal_places=3)
	large = models.DecimalField(max_digits=8, decimal_places=3)
	wide = models.DecimalField(max_digits=8, decimal_places=3)
