from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index_view ),
    path('api/todo/', views.ToDoListView.as_view()),
    path('api/todo/<int:pk>', views.ToDoDetailView.as_view()),
]
