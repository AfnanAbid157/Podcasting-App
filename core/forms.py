from django import forms
from .models import Podcasting

class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcasting
        fields = ["title", "description", "file", "thumbnail"]
