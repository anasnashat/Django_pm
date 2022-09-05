from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Project
from . import forms
# Create your views here.

class ListProjectsView(ListView):
    model = Project
    template_name = "projects/list.html"


class CreateProjectView(CreateView):
    model = Project
    form_class = forms.ProjectCreatForm
    template_name = "projects/creat.html"
    success_url = reverse_lazy("projects_list")
