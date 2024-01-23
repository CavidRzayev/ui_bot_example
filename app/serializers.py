from rest_framework import serializers


class StreamSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=500)
