from django.db import models
from django.core.mail import send_mail

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='food_items/')

    def __str__(self):
        return self.name

class Order(models.Model):
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    customer_email = models.EmailField()
    customer_location = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self): 
        return f'Order {self.id} - {self.food_item.name}'

    def save(self, *args, **kwargs):
        # Send email to the customer
        send_mail(
            'Order Confirmation',
            f'Your order for {self.food_item.name} has been received. It will be delivered soon.',
            'from@example.com',
            [self.customer_email],
            fail_silently=False,
        )
        super().save(*args, **kwargs)
