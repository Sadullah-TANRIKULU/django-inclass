from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # name unique olmalı
]

# return HttpResponse(data, content_type='application/json') json döndürmek için





