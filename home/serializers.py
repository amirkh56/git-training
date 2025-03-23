from rest_framework import serializers


class PerosnSerializer(serializers.Serializer) :
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()