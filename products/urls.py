# products/urls.py
from django.urls import path
from .views import ProductListCreateView, ProductDetailView, RegisterView,CategoryListView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path("categories/", CategoryListView.as_view(), name="category-list"),

]