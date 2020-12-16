from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<int:pk>/', views.edit, name='edit'),
    path('generate/', views.generate, name='generate'),
    path('', views.home, name='home'),
    path('<str:query>/', views.home, name='home'),
    path('delete/', views.delete, name="delete"),
    path('<str:query>/stats/', views.stats, name="stats"),

]