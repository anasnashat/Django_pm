from django.urls import path, include
from . import views
urlpatterns = [
    path("projects/list", views.ListProjectsView.as_view(), name="projects_list"),
    path("projects/creat", views.CreateProjectView.as_view(), name="projects_creat")
]