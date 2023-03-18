from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='custom_home'),
    path('profile/', views.profileView, name='custom_profile'),
    path('projects/', views.projectsView.as_view(), name='custom_projects'),
    path('purpose/', views.purposeView, name='custom_purpose'),
    path('login/', views.CustomLoginView, name='custom_testLogin'),
]
