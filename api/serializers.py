from rest_framework import serializers
from .models import Store,Product,Date


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_location']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name']
        
class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = ['date_id', 'date_field']