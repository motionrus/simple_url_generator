from rest_framework import serializers
from link.models import Link


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ['id', 'long_link', 'short_link']
        read_only_fields = ['id', "short_link"]
