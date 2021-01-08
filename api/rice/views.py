from rest_framework import viewsets
from .serializers import RiceSerializer, CurrySerializer
from .models import Curry, Rice


class RiceViewSet(viewsets.ModelViewSet):
    queryset = Rice.objects.filter(is_stock_avalable=True)
    serializer_class = RiceSerializer


class CurryViewSet(viewsets.ModelViewSet):
    queryset = Curry.objects.filter(is_stock_avalable=True)
    serializer_class = CurrySerializer
