from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order


def Home(request):
    orders = Order.objects.all()
    return render(request, 'index.html', {"orders": orders})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('name')
    serializer_class = OrderSerializer
