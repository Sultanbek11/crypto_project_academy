from rest_framework import serializers
from .models import Value


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ('title', 'price', 'volume', 'changes_12hour',)
