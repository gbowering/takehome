from forkrepo.models import RepoProfile
from django import forms

        
class RepoForm(forms.ModelForm):
    access_token = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = RepoProfile
        fields = ['repository','access_token']
