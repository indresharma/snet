from django.shortcuts import render, redirect
from .models import Profile
from .forms import RegisterForm
from django.views.generic import UpdateView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

class Register(View):
    form = RegisterForm()
    def get(self, request, *args, **kwargs):
        return render(request, 'users/register.html', {'form': self.form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(self.request.POST or None)
        if form.is_valid():
            user = form.save()
            user.profile.email = form.cleaned_data.get('email')
            user.save()
        return redirect('users:profile')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ('image', 'about_me', 'email', 'location')
    success_url = '/users/'


