from rest_framework import serializers
from.models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'name', 'image', 'price', 'unit',
                  'total', 'phone_no', 'adress', 'status')
