from django.urls import path
from .views import ProductListCreateView, ProductDetailView, show_settings

urlpatterns = [
    # your existing urls...
    path('debug-settings/', show_settings),
]


urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
