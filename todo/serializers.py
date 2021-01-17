from rest_framework import serializers
from .models import ToDoItem
class ToDoItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = 'id', 'text', 'done'
    done = serializers.BooleanField(required=True)
    # id = serializers.IntegerField()
    # text = serializers.CharField()
    # done = serializers.BooleanField()