from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)

    def _str_(self):
        return self.user.username

class Upload(models.Model):
    UPLOAD_TYPE_CHOICES = [
        ('cv', 'CV'),
        ('photo', 'Photo'),
        ('video', 'Video'),
        ('code', 'Code'),
        ('project', 'Project File'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    upload_type = models.CharField(max_length=20, choices=UPLOAD_TYPE_CHOICES)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return f"{self.user.username} - {self.title}"

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    repo_link = models.URLField(blank=True)
    cover = models.ImageField(upload_to='project_covers/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    files = models.ManyToManyField(Upload, blank=True)

    def _str_(self):
        return self.title

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    details = models.TextField(blank=True)

    def _str_(self):
        return f"{self.institution} ({self.user.username})"

class Hobby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def _str_(self):
        return self.name

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friend_of', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'friend')

class ChatMessage(models.Model):
    room_name = models.CharField(max_length=255)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return f"{self.room_name} {self.sender}: {self.message[:20]}"