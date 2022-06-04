
from django.urls import path
from .views import list, create_task, delete_task

urlpatterns = [
    path("", list),
    path("new_task/", create_task, name='create_task' ),
    path("delete_task/<int:id>", delete_task, name='delete_task' ),
]