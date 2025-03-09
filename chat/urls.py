from django.urls import path 
from .views import *

app_name = 'chat'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    # path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    # path('project/<int:pk>/add_message/', AddMessageView.as_view(), name='add_message'),
    
]