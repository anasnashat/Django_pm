from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.ListProjectsView.as_view(), name="projects_list"),
    path("projects/creat", views.CreateProjectView.as_view(), name="projects_creat"),
    path("projects/update/<int:pk>", views.UpdateProjectView.as_view(), name="projects_update"),
    path("projects/delete/<int:pk>", views.DeleteProjectView.as_view(), name="projects_delete"),
    path("task/creat", views.CreatTaskView.as_view(), name="task_creat"),
    path("task/edite/<int:pk>", views.UpdateTaskView.as_view(), name="task_update"),
    path("task/delete/<int:pk>", views.DeleteTaskView.as_view(), name="task_delete"),
]