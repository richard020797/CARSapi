from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Marca
from .serializers import MarcaSerializer
from django.http import Http404

class ListMarcas(APIView):
	def get(self,request):
		marcas = Marca.objects.all()
		serializer = MarcaSerializer(marcas, many=True)
		return Response(serializer.data)


	def post(self, request):
		serializer = MarcaSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailMarca(APIView):
	
	def get_object(self, pk):
		try:
			return Marca.objects.get(pk=pk)
		except Marca.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		marca = self.get_object(pk)
		serializer = MarcaSerializer(marca)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		marca = self.get_object(pk)
		serializer= MarcaSerializer(marca, data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		marca = self.get_object(pk)
		marca.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)