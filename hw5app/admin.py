from django.contrib import admin
from .models import Client, Product, Order

# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    search_fields = ['name', 'email', 'address']
    list_filter = ['name']
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity']
    search_fields = ['name', 'price']
    list_filter = ['price']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_price', 'quantity']
    search_fields = ['client__name', 'id']
    filter_horizontal = ['product']


    
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)