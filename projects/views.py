from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from . import models
from . import forms


# Create your views here.

class ListProjectsView(ListView):
    model = models.Project
    template_name = "projects/list.html"


class CreateProjectView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreatForm
    template_name = "projects/creat.html"
    success_url = reverse_lazy("projects_list")


class DeleteProjectView(DeleteView):
    model = models.Project
    template_name = "projects/delete.html"
    success_url = reverse_lazy("projects_list")


class UpdateProjectView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = "projects/update.html"

    # success_url = reverse_lazy("projects_list")
    def get_success_url(self):
        return reverse("projects_update", args=[self.object.id])


class CreatTaskView(CreateView):
    model = models.Task
    fields = ['description', 'project']
    http_method_names = ["post"]

    def get_success_url(self):
        return reverse("projects_update", args=[self.object.project.id])


class UpdateTaskView(UpdateView):
    model = models.Task
    fields = ["is_completed"]
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('projects_update', args=[self.object.project.id])


class DeleteTaskView(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse("projects_update", args=[self.object.project.id])
