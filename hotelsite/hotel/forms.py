from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['food_item', 'customer_name', 'customer_phone', 'customer_email', 'customer_location']
        widgets = {
            'food_item': forms.HiddenInput(),
        }
