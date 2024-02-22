from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    alert_message = serializers.CharField(read_only=True)
    class Meta:
        model = Customer
        fields = ['url', 'id', 'name', 'phone_number', 'alert_message']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'id', 'customer', 'item', 'amount', 'time']
