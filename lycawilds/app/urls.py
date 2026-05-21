from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todos, name='todos'),
    path('', views.news, name='news'),
    path('', views.guide, name='fieldguide'),
    path('', views.browse, name='browse'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # Built-in login, logout, password reset, etc.
    path('accounts/', include('django.contrib.auth.urls')),
    
]