from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Events,Participants
# from accounts.models import Profile
# from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, generics
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from rest_framework.permissions import IsAuthenticated
from event_app.serializers import *

# Create your views here.

#-------API to register for an Event---------------------------------------------------------------------------#
class NewEvent(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)
        response.data = {"message":"Your Event has been created successfully"}
        return response  
    
#---------API for Joining an Event----------------------------------------------------------------------------#
class JoinEventAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        event = Events.objects.get(id = pk)
        request.data['user'] = request.user.id
        Participants.objects.create(user = request.user, event_name = event)
        return Response({"message":"You have joined the event successfully"})
    
#---------Listing Event---------------------------------------------------------------------------------------#
class ListEvents(ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer


#---------Implemented Filterset for searching-----------------------------------------------------------------#   
class EventFilterSet(FilterSet):
    event_name = CharFilter(lookup_expr='contains')
    class Meta:
        model = Events
        fields = ['event_name']

#----------API for Searching Events----------------------------------------------------------------------------#

class SearchEvents(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilterSet

#---------Report-----------------------------------------------------------------------------------------------#
class ReportEvents(APIView):
    def get(self, request):
        event = Events.objects.prefetch_related('participants').filter(start_at__gte = request.data['date_from'], ends_at__lte = request.data['till_date'])
        data = EventsSerializer(event, many=True)
        return Response(data.data)