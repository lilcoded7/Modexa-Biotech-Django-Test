from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from accounts.serializers import RegisterUserSerializer, LoginUserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

# token blacklist import 
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.tokens import BlacklistedToken
from datetime import datetime
 

User = get_user_model()

# Create your views here.


class CreateUser(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'message':'Account Created! successfully'})


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'message':'Login successful'})
        return Response({'message':'login failed check email and password and login gain '})

        



# class TokenBlacklistBackend:
#     def __init__(self, *args, **kwargs):
#         self.token_backend = TokenBackend(*args, **kwargs)

#     def verify(self, token):
#         try:
#             # Check if the token is blacklisted
#             BlacklistedToken.objects.get(token=token)
#             return False
#         except BlacklistedToken.DoesNotExist:
#             # Verify the token's signature and expiration
#             return self.token_backend.verify(token)

#     def get_validated_token(self, raw_token):
#         return self.token_backend.get_validated_token(raw_token)

#     def check_blacklist(self, token):
#         try:
#             # Check if the token is blacklisted
#             BlacklistedToken.objects.get(token=token)
#             return True
#         except BlacklistedToken.DoesNotExist:
#             return False