from rest_framework import serializers
from .models import Task
from projects.models import Project

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ["assigned_to"]
    
    def check(self, value):
        user = self.context["request"].user

        if value.owner != user:
            raise serializers.ValidationError("Nie mozesz dodac nic do innego projektu!!")
            
        return value
        