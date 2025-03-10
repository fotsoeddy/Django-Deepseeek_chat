from django.shortcuts import  render,get_object_or_404
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from django.views import View
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
    
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'chat/project_form.html'
    success_url = reverse_lazy('chat:project_list')
    def form_valid(self, form):
        messages.success(self.request, 'Project updated successfully')
        return super().form_valid(form)
    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
    
class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'chat/project_delete.html'
    success_url = reverse_lazy('chat:project_list')
    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Project deleted successfully')
        return super().delete(request, *args, **kwargs)
    

class ChatView(LoginRequiredMixin, View):
    template_name = 'chat/chat.html'

    def get(self, request, project_id, *args, **kwargs):
        project = get_object_or_404(Project, pk=project_id, owner=request.user)
        messages = project.chatmessage_set.all()
        projects = Project.objects.all()  # Fetch all projects

        context = {
            'project': project,
            'messages': messages,
            'projects': projects,  # Sidebar projects
        }
        return render(request, self.template_name, context)
   







