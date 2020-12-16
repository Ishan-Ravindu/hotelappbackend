from django.urls import path, include

urlpatterns = [
    path('banner/', include('api.banner.urls')),
    path('product/', include('api.product.urls')),
]
