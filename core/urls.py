from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home_view'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.login, name='login'),
    path('ticket_view/', views.ticket_view, name='ticket_view'),
]

