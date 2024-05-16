from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_image_product, name='upload_image_product'),
    path('clients/<int:client_id>/', views.client_orders, name='client_orders'),
    path('clients/', views.found_client_id, name='found_client_id'),
]