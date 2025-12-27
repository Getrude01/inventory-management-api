# products/views.py
from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwner

class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        # Users only see their own products
        return Product.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically assign the logged-in user as owner
        serializer.save(owner=self.request.user)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        # Users can only access their own products
        return Product.objects.filter(owner=self.request.user)
