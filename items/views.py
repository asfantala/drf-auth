from django.shortcuts import render
from rest_framework import generics
from .models import Item , Post
from .serializers import ItemSerializer,PostSerializer
from rest_framework.permissions import AllowAny , IsAuthenticated
from .permissions import IsOwnerOrReadOnly
# Create your views here.

# ListAPIView
class ItemsList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

# RetrieveAPIView RetrieveUpdateAPIView
class ItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwnerOrReadOnly]



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

