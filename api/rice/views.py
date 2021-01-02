from rest_framework import viewsets
from .serializers import ImageSerializer, RiceSerializer, CurrySerializer
from .models import Curry, Image, Rice


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class RiceViewSet(viewsets.ModelViewSet):
    queryset = Rice.objects.all()
    serializer_class = RiceSerializer


class CurryViewSet(viewsets.ModelViewSet):
    queryset = Curry.objects.all()
    serializer_class = CurrySerializer
