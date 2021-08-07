from django.http import response
from django.shortcuts import render
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Employeviewset(viewsets.ModelViewSet):
    queryset=Worker.objects.all()
    serializer_class=EmployeSerializers


