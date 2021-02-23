from django.urls import path, include
from .views import apiHome

urlpatterns = [
    path('', apiHome, name="apiHome"),
    path('banner/', include('api.banner.urls')),
    path('product/', include('api.product.urls')),
    path('order/', include('api.order.urls')),
    path('rice/', include('api.rice.urls')),
    path('mobile/', include('api.mobile.urls')),
]
