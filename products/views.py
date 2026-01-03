# products/views.py
from rest_framework import generics, permissions
from rest_framework.generics import RetrieveAPIView
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwner

class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Product.objects.none()

        # Users only see their own products
        return Product.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically assign the logged-in user as owner
        serializer.save(owner=self.request.user)

class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # THIS FIXES SWAGGER
        if getattr(self, 'swagger_fake_view', False):
            return Product.objects.none()

        return Product.objects.filter(owner=self.request.user)

