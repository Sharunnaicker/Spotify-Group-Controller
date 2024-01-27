from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
# Where we will be writing end points; end points are locations on the web 
# python3 ./manage.py runserver

class RoomView(generics.ListAPIView): 
    queryset = Room.objects.all() 
    serializer_class = RoomSerializer