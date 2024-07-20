from django.contrib import admin
from .models import FoodItem, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('food_item', 'customer_name', 'customer_phone', 'customer_email', 'customer_location', 'order_date', 'status')
    list_filter = ('status',)
    search_fields = ('customer_name', 'customer_email', 'food_item__name')

admin.site.register(FoodItem)
admin.site.register(Order, OrderAdmin)
