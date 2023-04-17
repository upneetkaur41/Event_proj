from django.shortcuts import render
from rest_framework import serializers,views
from rest_framework.serializers import ModelSerializer
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login,logout
from event_app.models import Participants
from rest_framework.views import APIView
from accounts.serializers import *
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

# Create your views here.
#-----------------------------------------------------------------------------------------------------#

#------Creating/registering the user------------------------------------------------------------------# 
class CreateNewUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {"message":"User Registered Successfully"}
        return response
    

#--------------Listing the users---------------------------------------------------------------------#  
class ListUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer


#-----------------login user------------------------------------------------------------#
class LoginUser(views.APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username,password=password)
        login(request, user)
        u = User.objects.get(username = username)
        token = Token.objects.create(user = u)
        serializer = Userserializer(user)
        return Response({"data":serializer.data, "Token":token.key,})
    

#---------------logout user-------------------------------------------------------------#
class LogoutUser(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        logout(request)
        return Response({"data":"Logout Successful"})

#--------------change password----------------------------------------------------------#
class NewPassword(views.APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        u = User.objects.get(username=request.user)
        u.set_password(request.data['password'])
        u.save()
        return Response({"data":"Password Changed Successfully"})
    

 
#-------getting data as a Profile-------------------------------------------------------------------------------#
class Profile(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = User.objects.get(id = request.user.id)
        data = {
            "user":user.username,
            "Email":user.email
        }
        event_data = Participants.objects.filter(user = request.user)
        events = []
        for i in event_data:
            events.append(i.event_name.event_name)
        data['Events'] = events
        return Response(data)
