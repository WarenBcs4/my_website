from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education_list, name='education'),
    path('hobbies/', views.hobbies_list, name='hobbies'),
    path('friends/', views.friends_list, name='friends'),
    path('projects/', views.projects_list, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('upload/', views.upload_create, name='upload'),
    path('create-project/', views.create_project, name='create_project'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]