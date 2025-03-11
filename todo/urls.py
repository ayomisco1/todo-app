from django.urls import path
from .views import list_todo

urlpatterns = [
    path('', list_todo, name="todo-list")

]