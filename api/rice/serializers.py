from rest_framework import serializers
from .models import Curry, Rice


class RiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Rice
        fields = ('id', 'name', 'price', 'is_stock_avalable')


class CurrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Curry
        fields = ('id', 'name', 'price',  'is_stock_avalable')
