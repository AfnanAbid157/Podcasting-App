from django.shortcuts import render
from core.models import Podcasting


def home(request):
    podcasts = Podcasting.objects.all()[:3]  # use lowercase variable name
    return render(request, "index.html", context={"podcasts": podcasts})
