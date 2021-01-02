from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_stock_avalable=True)
    serializer_class = ProductSerializer
