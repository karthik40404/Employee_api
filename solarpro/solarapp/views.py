from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.

class empv(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=Emp
    