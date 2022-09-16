from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class ListProjectsView(LoginRequiredMixin, ListView):
    model = models.Project
    template_name = "projects/list.html"
    paginate_by = 6

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {"ser_id": self.request.user}
        q = self.request.GET.get('q', None)
        if q:
            where['title__contains'] = q
        return query_set.filter(**where)


class CreateProjectView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectCreatForm
    template_name = "projects/creat.html"
    success_url = reverse_lazy("projects_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteProjectView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Project
    template_name = "projects/delete.html"
    success_url = reverse_lazy("projects_list")

    def test_func(self):
        return self.get_object().user_id == self.request.user


class UpdateProjectView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = "projects/update.html"

    def test_func(self):
        return self.get_object().user_id == self.request.user

    # success_url = reverse_lazy("projects_list")
    def get_success_url(self):
        return reverse("projects_update", args=[self.object.id])


class CreatTaskView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Task
    fields = ['description', 'project']
    http_method_names = ["post"]

    def test_func(self):
        project_id = self.request.POST.get('project', '')
        return models.Project.objects.get(pk=project_id) == self.request.user.id

    def get_success_url(self):
        return reverse("projects_update", args=[self.object.project.id])


class UpdateTaskView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Task
    fields = ["is_completed"]
    http_method_names = ['post']

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('projects_update', args=[self.object.project.id])


class DeleteTaskView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Task

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse("projects_update", args=[self.object.project.id])
