# bundles/serializers.py
from rest_framework import serializers
from .models import Bundle
from menu.serializers import MenuItemSerializer  # Assuming you want to include menu items

class BundleSerializer(serializers.ModelSerializer):
    # If you want to include detailed information about related menu items or categories
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Or for more detailed information
    # categories = CategorySerializer(many=True, read_only=True)
    
    # Example of including menu items directly (customize based on your model structure)
    menu_items = MenuItemSerializer(many=True, read_only=True, source='menuitem_set')
    
    class Meta:
        model = Bundle
        fields = ['id', 'name', 'description', 'categories', 'menu_items']
        # Adjust 'fields' to include the fields you want in your API.
        # If you're not including menu items directly, remove 'menu_items' from the list.
