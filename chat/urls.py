from django.urls import path 
from .views import ProjectCreateView, ProjectListView

app_name = 'chat'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    # path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    # path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    # path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    # path('project/<int:pk>/add_message/', AddMessageView.as_view(), name='add_message'),
    
]