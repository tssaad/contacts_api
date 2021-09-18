from django.shortcuts import render
from django.conf import settings
from django.contrib import auth

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

import jwt

from .serializers import UserSerializer, LoginAPIViewSerializer

class RegisterAPIView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #serializer.is_valid(raise_exception=True)
        #serializer.save()

        #return Response(serializer.data, status=status.HTTP_200_OK)

class LoginAPIView(GenericAPIView):
    serializer_class = LoginAPIViewSerializer

    def post(self, request):
        
        data=request.data
        username=data.get('username','')
        password=data.get('password','')

        user = auth.authenticate(username=username, password=password)

        if user:
            user_data = {"username" : user.username}
            auth_token = jwt.encode(user_data, key=settings.JWT_SECRET_KEY, algorithm="HS256")
            serializer = UserSerializer(user)
            context = {
                'user' : serializer.data,
                'token' : str(auth_token),
            }
            return Response(context, status=status.HTTP_200_OK)
        return Response({'detail':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
