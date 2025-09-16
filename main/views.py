from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Project, Upload, Education, Hobby, Friend, ChatMessage, Profile
from .forms import UploadForm, ProjectForm, ProfileForm
from django.contrib.auth.models import User

def home(request):
    projects = Project.objects.order_by('-created_at')[:6]
    latest_uploads = Upload.objects.order_by('-created_at')[:6]
    return render(request, 'main/home.html', {'projects': projects, 'latest_uploads': latest_uploads})

def about(request):
    return render(request, 'main/about.html')

    return render(request, 'main/education_list.html', {'educations': educations})


def education_list(request):
    educations = Education.objects.all().order_by('-start_date')  # or filter by user if needed
    return render(request, 'main/education_list.html', {
        'educations': educations
    })



def hobbies_list(request):
    Hobby= Hobby.objects.filter(user=request.user) if request.user.is_authenticated else Hobby.objects.none()
    return render(request, 'main/hobbies_list.html', {'hobbies': hobbies})

def friends_list(request):
    friends = []
    if request.user.is_authenticated:
        friend_relations = Friend.objects.filter(user=request.user)
        friends = [fr.friend for fr in friend_relations]
    return render(request, 'main/friends_list.html', {'friends': friends})

def projects_list(request):
    project_list = Project.objects.all().order_by('-created_at')
    paginator = Paginator(project_list, 5)  # 5 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/projects_list.html', {'page_obj': page_obj})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'main/project_detail.html', {'project': project})

@login_required
def upload_create(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = request.user
            upload.save()
            return redirect('projects')
    else:
        form = UploadForm()
    return render(request, 'main/upload_form.html', {'form': form})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            form.save_m2m()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'main/create_project.html', {'form': form})

@login_required
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'main/profile_edit.html', {'form': form})

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = getattr(user, 'profile', None)
    projects = Project.objects.filter(user=user).order_by('-created_at')[:10]
    return render(request, 'main/profile.html', {'profile': profile, 'projects': projects, 'user_profile': user})

@login_required
def chat_room(request, room_name):
    messages = ChatMessage.objects.filter(room_name=room_name).order_by('timestamp')[:200]
    return render(request, 'main/chat_room.html', {'room_name': room_name, 'messages': messages})


def projects_list(request):
    project_list = Project.objects.all().order_by('-created_at')
    upload_list = Upload.objects.all().order_by('-created_at')

    # Paginate both separately
    project_paginator = Paginator(project_list, 6)  # 6 projects per page
    upload_paginator = Paginator(upload_list, 6)    # 6 uploads per page

    project_page_number = request.GET.get('projects_page')
    upload_page_number = request.GET.get('uploads_page')

    project_page_obj = project_paginator.get_page(project_page_number)
    upload_page_obj = upload_paginator.get_page(upload_page_number)

    return render(request, 'main/projects_list.html', {
        'project_page_obj': project_page_obj,
        'upload_page_obj': upload_page_obj,
    })
