from rest_framework import viewsets
from .models import Order, Customer

from order_project.order_service.serializers import OrderSerializer, CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed.
    """
    queryset = Order.objects.all().order_by('time')
    serializer_class = OrderSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
