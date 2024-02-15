from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    id = serializers.IntegerField()
    is_bot = serializers.BooleanField()
    language_code=serializers.CharField(max_length=10)
    username = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=15)