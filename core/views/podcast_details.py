from django.shortcuts import render, get_object_or_404
from core.models import Podcasting

def podcast_details(request, slug):
    podcast = get_object_or_404(Podcasting, slug=slug)
    context = {"podcast": podcast}
    return render(request, "podcast_details.html", context)
