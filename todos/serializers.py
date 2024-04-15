from rest_framework import serializers
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'owner',
        )
        model = models.Todo