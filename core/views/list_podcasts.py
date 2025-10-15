from django.shortcuts import render
from core.models import Podcasting

def list_podcasts(request):
    podcasts = Podcasting.objects.all()  # ✅ 'objects' (not 'object')
    return render(request, "list_podcasts.html", {"podcasts": podcasts})  # ✅ file name & context syntax
