from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass

    # add additional fields in here

    def __str__(self):
        return self.username

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_owner = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='created_projects')

    def __str__(self):
        return self.name

class Ticket(models.Model):
    status_choices = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='assigned_tickets')
    created_by = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='created_tickets')
    status = models.CharField(max_length=100, choices=status_choices, default='Open')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tickets')

    def __str__(self):
        return self.title


