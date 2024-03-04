from django.shortcuts import render
from .models import Position, Staff
from .serializers import StaffSerializer, PositionSerializer
from rest_framework.generics import ListCreateAPIView



class StaffApiView(ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class PositionApiView(ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer




