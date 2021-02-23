from rest_framework import viewsets
from .serializers import MobileSerializer
from .models import Mobile

# Create your views here.


class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
