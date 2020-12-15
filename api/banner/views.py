from rest_framework import viewsets
from .serializers import BannerSerializer
from .models import Banner

# Create your views here.


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all().order_by('name')
    serializer_class = BannerSerializer
