from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.urls import reverse_lazy


class ProjectListView( LoginRequiredMixin,  ListView):
    model = Project
    template_name = 'chat/project_list.html'
    context_object_name = 'projects'
    

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user).order_by('created_at')

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'chat/project_form.html'
    success_url = reverse_lazy('chat:project_list')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, 'Project created successfully')
        return super().form_valid(form) 







