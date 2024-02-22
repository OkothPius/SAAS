import requests
from django.db import models
from django.conf import settings

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20) # format should be +25471912xxxx
    alert_message = models.CharField(max_length=255, default="Account created! Make an order today!")

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item} - {self.customer.name}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        url = "https://api.sandbox.africastalking.com/version1/messaging"
        
        headers = {
            'ApiKey': settings.AT_API_KEY,  # Use your Africa's Talking API key
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }

        data = {
            'username': settings.AT_USERNAME,  # Use your Africa's Talking username
            'from': settings.AT_SHORTCODE,  # Set your sender ID
            'message': f"Niaje {self.customer.name}, Your order ({self.item}) has been created!",
            'to': self.customer.phone_number 
        }

        try:
            response = requests.post(url=url, headers=headers, data=data)
            print(response.json())
        except Exception as e:
            print(f"Failed to send SMS: {e}")

        self.customer.alert_message = data['message']
        self.customer.save()