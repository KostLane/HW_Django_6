from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from datetime import timedelta
from .models import Client, Product, Order
import django.utils.timezone

# Create your views here.

def index(request):
    
    html = """
    <h1>Главная страница</h1>
    <p>Задание №4:</p>
    <p>Измените модель продукта, добавьте поле для хранения фотографии продукта.</p>
    <p>Создайте форму, которая позволит сохранять фото.</p>
    <br></br>
    <p>Задание №5:</p>
    <p>Настройте под свои нужды вывод информации о клиентах,</p> 
    <p>товарах и заказах на страницах вывода информации об объекте и вывода списка объектов.</p>
    <p>Задание №6:</p>
    <p>Настроить работу проекта на сервере.<p>
    """
    title = "Задание №4, №5, №6"
    return render(request, 'hw5app/index.html', {'html': html, 'title': title})

def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    request.session['client_id'] = client_id

    now = django.utils.timezone.now()

    products_by_time = {
        'week': set(),
        'month': set(),
        'year': set(),
        'count_orders_week': 0,
        'count_orders_month': 0,
        'count_orders_year': 0,
        'sum_orders_week': 0,
        'sum_orders_month': 0,
        'sum_orders_year': 0,
    }

    for order in orders:
        products = Product.objects.filter(order=order)

        for product in products:
            if order.data_ordered >= now - timedelta(days=7):
                products_by_time['week'].add(product)
                products_by_time['count_orders_week'] += 1
                products_by_time['sum_orders_week'] += order.total_price * order.quantity
            elif order.data_ordered >= now - timedelta(days=30):
                products_by_time['month'].add(product)
                products_by_time['count_orders_month'] += 1
                products_by_time['sum_orders_month'] += order.total_price * order.quantity
            elif order.data_ordered >= now - timedelta(days=365):
                products_by_time['year'].add(product)
                products_by_time['count_orders_year'] += 1
                products_by_time['sum_orders_year'] += order.total_price * order.quantity

    return render(request, 'hw5app/client_orders.html', {'client': client, 'products_by_time': products_by_time, 'orders': orders})

def upload_image_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            new_product = product_form.save()
            return render(request, 'hw5app/upload_image.html', {'answer': 'Данные успешно отправлены на сервер!'})
    else:
        product_form = ProductForm()
    return render(request, 'hw5app/upload_image.html', {'product_form': product_form})

def found_client_id(request):
    return render(request, 'hw5app/client_id.html')