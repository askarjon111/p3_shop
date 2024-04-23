from django.urls import path

from shop.views import home_view, products_view, single_product_view


urlpatterns = [
    path('', home_view, name='home'),
    path('shop/', products_view, name='products'),
    path('shop/<int:pk>/', single_product_view, name='single_product'),
]
