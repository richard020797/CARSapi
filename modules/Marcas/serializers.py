from rest_framework import serializers
from modules.Autos.serializers import AutoSerializer
from modules.Sucursales.serializers import SucursalSerializer
from .models import Marca

class MarcaSerializer(serializers.ModelSerializer):

	#cars = serializers.StringRelatedField(many=True) #String serializer brings just the related field
	cars = AutoSerializer(many=True, read_only=True) #Nested serializer
	#stores = serializers.StringRelatedField(many=True)
	stores = SucursalSerializer(many=True, read_only=True) #Nested serializer
	
	class Meta:
		model = Marca
		fields = ('name','trustScore','country','cars','stores')

