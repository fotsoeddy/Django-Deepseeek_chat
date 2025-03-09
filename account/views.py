from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from.forms import CustomSignupForm, CustomLoginForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout


class SignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request.user)
        return redirect(self.success_url)

class CustomLoginForm(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'account/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
