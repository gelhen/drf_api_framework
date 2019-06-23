from rest_framework import serializers
from vmtodo.drf.models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    # Meta é uma classe para configurar uma classe,
    class Meta:
        model = Tasks
        fields = ('id', 'task', 'disable', 'created_at')
