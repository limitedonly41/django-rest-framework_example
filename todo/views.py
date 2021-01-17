from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ToDoItem
from .serializers import ToDoItemSerializers


def index_view(request):
    return HttpResponse('<h1>Hello ToDo App!</h1>')


class ToDoListView(APIView):

    def get(self, request):
        items = list(ToDoItem.objects.all())
        serializer = ToDoItemSerializers(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoDetailView(APIView):

    def get(self, request, pk):
        # todo = ToDoItem.objects.get(pk=pk)
        todo = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerializers(todo)
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = get_object_or_404(ToDoItem, pk=pk)
        serializer = ToDoItemSerializers(todo)
        data = serializer.data
        todo.delete()
        return Response(data)
