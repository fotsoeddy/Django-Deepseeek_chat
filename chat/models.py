from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects', verbose_name='Owner')
    name = models.TextField(verbose_name='Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_at']

class ChatMessage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Project')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    message = models.TextField(verbose_name='Message')
    response = models.TextField(blank=True, null=True, verbose_name='Response')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    def __str__(self):
        return f"{self.user.username}: {self.message[:50]}..."

    class Meta:
        verbose_name = 'Chat Message'
        verbose_name_plural = 'Chat Messages'
        ordering = ['-timestamp']