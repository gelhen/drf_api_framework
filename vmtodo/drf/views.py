from vmtodo.drf.models import Tasks
from vmtodo.drf.serializers import TaskSerializer
from rest_framework import generics


class TaskList(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

