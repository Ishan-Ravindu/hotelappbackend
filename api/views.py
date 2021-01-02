from django.shortcuts import render
from django.http import HttpResponse


def apiHome(request):
    return HttpResponse('"product=/api/product/","orders=/api/order","banner=/api/banner/"')
