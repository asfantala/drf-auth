from rest_framework import serializers
from .models import Item,Post

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'user', 'name', 'description', 'created_at', 'updated_at', 'quantity')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
