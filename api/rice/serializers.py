from rest_framework import serializers
from .models import Curry, Image, Rice


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Image
        fields = ('id', 'name', 'image', 'category')


class RiceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Rice
        fields = ('id', 'name', 'price', 'category', 'is_stock_avalable')


class CurrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Curry
        fields = ('id', 'name', 'price', 'category', 'is_stock_avalable')
