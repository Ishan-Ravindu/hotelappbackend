from rest_framework import serializers
from.models import Banner


class BannerSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Banner
        fields = ('id', 'name', 'image')
