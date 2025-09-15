from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  # 'todo/'를 제거하고 ''로 변경
    path('<int:todo_id>/', views.todo_info, name='todo_info'), # 'todo/'를 제거
]