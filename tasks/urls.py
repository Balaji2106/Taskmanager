from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, task_list_view, task_detail_view, task_form_view, task_delete_view

router = DefaultRouter()
router.register(r'api/tasks', TaskViewSet)

urlpatterns = [
    path('', task_list_view, name='task_list'),              # List view
    path('task/<int:pk>/', task_detail_view, name='task_detail'),  # Details view
    path('task/form/', task_form_view, name='task_add'),      # Add task form
    path('task/form/<int:pk>/', task_form_view, name='task_edit'),  # Edit task form
    path('task/delete/<int:pk>/', task_delete_view, name='task_delete'),  # Delete task
    path('', include(router.urls)),                          # API routes
]
