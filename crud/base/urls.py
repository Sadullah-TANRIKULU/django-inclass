from django.urls import path
from .views import index, student_add, student_delete, student_detail, student_list, student_update

urlpatterns = [
    path('', index, name='index'), # index view e ulaşmada name=index unique olarak kullanılır.
    path('list/',student_list , name='list'),
    path('add/',student_add , name='add'),
    path('update/<int:id>',student_update , name='update'),
    path('delete/<int:id>',student_delete , name='delete'),
    path('student/<int:id>', student_detail, name="detail"),
]
