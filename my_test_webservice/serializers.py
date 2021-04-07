from rest_framework import serializers
from my_test_webservice.models import Links


class LinksSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    link = serializers.CharField(max_length=60, required=True)
    short = serializers.CharField(max_length=12, required=False, allow_blank=True)
    active = serializers.BooleanField(default=False, required=False)

    def create(self, validated_data):
        return Links.objects.create(**validated_data)
