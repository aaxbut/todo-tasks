from rest_framework import serializers, validators
from apps.tasks.models import Tasks


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for ``Tasks`` model"""

    class Meta:
        model = Tasks
        fields = (
            'name',
        )
