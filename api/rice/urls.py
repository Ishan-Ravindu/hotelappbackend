from rest_framework import routers
from django.urls import path, include
from . import views

imageRouter = routers.DefaultRouter()
imageRouter.register('image', views.ImageViewSet)

riceRouter = routers.DefaultRouter()
riceRouter.register('rice', views.RiceViewSet)

curryRouter = routers.DefaultRouter()
curryRouter.register('curry', views.CurryViewSet)

urlpatterns = [
    path('', include(imageRouter.urls)),
    path('', include(riceRouter.urls)),
    path('', include(curryRouter.urls)),
]
