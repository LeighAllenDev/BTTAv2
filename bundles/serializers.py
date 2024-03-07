# bundles/serializers.py

from rest_framework import serializers
from .models import Bundle
from menu.serializers import MenuItemSerializer  # Assuming you have this serializer defined

class BundleSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)  # Nested serialization for menu items

    class Meta:
        model = Bundle
        fields = ['id', 'name', 'description', 'items']
