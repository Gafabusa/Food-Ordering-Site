from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import FoodItem, Order
from .forms import OrderForm

def index(request): 
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def book(request):
    return render(request, 'book.html', {})

def menu(request):
    food_items = FoodItem.objects.all()  # Fetch all food items
    return render(request, 'menu.html', {'food_items': food_items})

def order_food(request, item_id):
    food_item = get_object_or_404(FoodItem, id=item_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.food_item = food_item
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm(initial={'food_item': food_item.id})
    
    return render(request, 'order_form.html', {'form': form, 'food_item': food_item})

def order_success(request):
    return render(request, 'order_success.html')
