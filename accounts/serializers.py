from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email (value) :
    if 'admin' in value :
        raise serializers.ValidationError('admin cant be in email')


class UserRegisterSerializer (serializers.ModelSerializer) :
    password2 = serializers.CharField(required = True, write_only = True)

    class Meta :
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only' : True},
            'email' : {'validators' : [clean_email]},
        }

    def create (self, validated_data) :
        del validated_data['password2']
        return User.objects.create_user(**validated_data) 


    def validate_username (self, value) :
        if value == "admin" :
            raise serializers.ValidationError("username cant be 'admin' !!")
        return value
        

    def validate(self, data) :
        if data['password'] != data['password2'] :
            raise serializers.ValidationError("Password must match !!")
        return data
    


class UserSerializer(serializers.ModelSerializer) :
    class Meta :
        model = User
        fields = "__all__"