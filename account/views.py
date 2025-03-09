from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomSignupForm, CustomLoginForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout

class SignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('chat:project_list')  # Make sure this matches your URL name

    def form_valid(self, form):
        user = form.save()  # Get the user object from the form
        login(self.request, user)  # Correct syntax: login(request, user)
        return redirect(self.success_url)  # Or redirect to another page like 'chat:project_list'

class CustomLoginView(LoginView):  # Renamed for clarity
    authentication_form = CustomLoginForm
    template_name = 'account/login.html'

def logout_view(request):
    logout(request)
    return redirect('account:login')