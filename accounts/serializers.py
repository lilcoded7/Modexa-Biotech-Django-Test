from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True)
    class Meta:
        model = User 
        fields = ['username', 'email', 'phone', 'password', 'password2']


    def create(self, validated_data):
        password = validated_data.get("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user




class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            data['access_token'] = str(refresh.access_token)
            data['refresh_token'] = str(refresh)
            return data
        raise serializers.ValidationError("Incorrect credentials")

