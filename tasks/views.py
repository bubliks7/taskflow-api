from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class TaskListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(assigned_to=user)
        
        status = self.request.query_params.get("status")
        project = self.request.query_params.get("project")
        priority = self.request.query_params.get("priority")

        if status:
            queryset = queryset.filter(status=status)
        if project:
            queryset = queryset.filter(project=project)
        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset
        # return Task.objects.filter(project__owner=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(
            Q(owner=self.request.user) | Q(members=self.request.user)
        ).distinct() 
