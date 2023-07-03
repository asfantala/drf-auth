from django.shortcuts import render
from rest_framework import generics
from .models import Item 
from .serializers import ItemSerializer

# Create your views here.

# ListAPIView
class ItemsList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# RetrieveAPIView RetrieveUpdateAPIView
class ItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer