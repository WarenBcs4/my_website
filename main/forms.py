from django import forms
from .models import Upload, Project, Profile

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['title', 'upload_type', 'file', 'description']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'repo_link', 'cover', 'files']
        widgets = {
            'files': forms.CheckboxSelectMultiple,
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'avatar', 'twitter', 'github', 'linkedin', 'website']