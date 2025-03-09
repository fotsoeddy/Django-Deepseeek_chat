from django.shortcuts import render,redirect
from django.views.generic import CreateView
from.forms import CustomSignupForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate


class SignupView(CreateView):
    form_class = CustomSignupForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request.user)
        return redirect(success_url)
