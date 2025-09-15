"""
URL configuration for config project.
...
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')), # todo 앱의 urls.py를 포함시킵니다.
]