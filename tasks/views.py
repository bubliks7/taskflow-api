from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializers

# Create your views here.

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
