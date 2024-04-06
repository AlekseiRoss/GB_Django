from django.urls import path
from .views import ProductsClientView

urlpatterns = [
    path('products/<int:client_id>/', ProductsClientView.as_view(),
         name='client_products')
]