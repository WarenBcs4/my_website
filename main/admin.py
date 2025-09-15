from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, Upload, Project, Education, Hobby, Friend, ChatMessage


admin.site.register(Profile)
admin.site.register(Upload)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Hobby)
admin.site.register(Friend)
admin.site.register(ChatMessage)