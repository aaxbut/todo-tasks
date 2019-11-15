from rest_framework import (
    mixins,
    viewsets,
)
from rest_framework.permissions import IsAuthenticated
from apps.tasks import models, serializers


class TasksViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = [IsAuthenticated, ]
    queryset = models.Tasks.objects.all()
    serializer_class = serializers.TaskSerializer
