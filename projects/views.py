from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class ListProjectsView(LoginRequiredMixin, ListView):
    model = models.Project
    template_name = "projects/list.html"
    paginate_by = 2

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self.request.GET.get('q', None)
        if q:
            where['title__contains'] = q
        return query_set.filter(**where)


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectCreatForm
    template_name = "projects/creat.html"
    success_url = reverse_lazy("projects_list")


class DeleteProjectView(LoginRequiredMixin, DeleteView):
    model = models.Project
    template_name = "projects/delete.html"
    success_url = reverse_lazy("projects_list")


class UpdateProjectView(LoginRequiredMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = "projects/update.html"

    # success_url = reverse_lazy("projects_list")
    def get_success_url(self):
        return reverse("projects_update", args=[self.object.id])


class CreatTaskView(LoginRequiredMixin, CreateView):
    model = models.Task
    fields = ['description', 'project']
    http_method_names = ["post"]

    def get_success_url(self):
        return reverse("projects_update", args=[self.object.project.id])


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = models.Task
    fields = ["is_completed"]
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('projects_update', args=[self.object.project.id])


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse("projects_update", args=[self.object.project.id])
