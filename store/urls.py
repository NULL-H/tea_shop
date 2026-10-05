from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('orders/', views.orders_view, name='orders'),
]