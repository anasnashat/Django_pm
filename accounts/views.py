from django.contrib.auth import login
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

from accounts.forms import UserRegisterForm, ProfileForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = "registration/register.html"

    # success_url = reverse_lazy("login")
    def get_success_url(self):
        login(self.request, self.object)
        return reverse_lazy('projects_list')


@login_required
def get_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
        return render(request, 'registration/profile.html', {
            "form": form
        })
