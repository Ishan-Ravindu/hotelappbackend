from rest_framework import routers
from django.urls import path, include
from . import views


riceRouter = routers.DefaultRouter()
riceRouter.register('rice', views.RiceViewSet)

curryRouter = routers.DefaultRouter()
curryRouter.register('curry', views.CurryViewSet)

urlpatterns = [

    path('', include(riceRouter.urls)),
    path('', include(curryRouter.urls)),
]
