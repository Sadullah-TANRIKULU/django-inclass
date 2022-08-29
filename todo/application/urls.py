from django.urls import path, include
from .views import home, todo_delete, todo_update

urlpatterns = [
    path('', home, name="home"),
    # path('add/', todo_add, name="add"),
    path('delete/<int:id>', todo_delete, name="delete"),
    path('update/<int:id>', todo_update, name="update"),
]