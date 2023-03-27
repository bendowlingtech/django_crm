from django.contrib import admin
from django.urls import path, include
import views
urlpatterns = [
    path('', views.home, name='home_view'),
    path('signup', views.signup, name='signup_view'),
    path('signin', views.signin, name='signin_view'),
    path('ticket_view', views.ticket_view, name='ticket_view'),
]

