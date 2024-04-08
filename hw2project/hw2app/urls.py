from django.urls import path
from .views import ProductsClientView, upload_image

urlpatterns = [
    path('products/<int:client_id>/', ProductsClientView.as_view(),
         name='client_products'),
    path('products/upload/<int:product_id>', upload_image,
         name='upload_image')
]
