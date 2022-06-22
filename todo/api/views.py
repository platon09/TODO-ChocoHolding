from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from todo.api.serializers import TaskSerializer
from todo.models import Task


class TodoViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        else:
            self.queryset.filter(author=self.request.user)