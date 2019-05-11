from django.contrib import admin
from django.urls import path
from.import views



urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.AddTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path("delete", views.deleteCompleted, name="delete"),
    path("deleteall", views.deleteAll, name="deleteall"),
    path('uncomplete/<todo_id>', views.uncompleteTodo, name='uncomplete'),
]
