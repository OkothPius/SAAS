import pytest
from unittest.mock import patch
from django.conf import settings
from django.test import RequestFactory
from order_project.order_service.models import Customer, Order
from order_project.order_service.views import OrderViewSet

@pytest.mark.django_db
class TestOrderCreation:
    @patch('requests.post')
    def test_order_creation(self, mock_post):
        # Create a customer
        customer = Customer.objects.create(name="John Doe", phone_number="+254719121890")

        # Create an order
        order = Order.objects.create(customer=customer, item="Test Item", amount=10.00)

        # Mock the response from the Africa's Talking API
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {'status': 'success'}

        # Refresh customer object to get the updated alert_message
        customer.refresh_from_db()

        # Assert the order was created successfully
        assert order.pk is not None

        mock_post.assert_called_once_with(
            url="https://api.sandbox.africastalking.com/version1/messaging",
            headers={
                'ApiKey': settings.AT_API_KEY,  
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json'
            },
            data={
                'username': settings.AT_USERNAME,  
                'from': settings.AT_SHORTCODE,  
                'message': f"Niaje {customer.name}, Your order ({order.item}) has been created!",
                'to': customer.phone_number
            }
        )

        assert customer.alert_message == f"Niaje {customer.name}, Your order ({order.item}) has been created!"
