from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views.home import home
from core.views.upload_podcast import upload_podcast
from core.views.list_podcasts import list_podcasts
from core.views.podcast_details import podcast_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('auth/', include('accounts.urls')),
    path('upload/', upload_podcast, name="upload_podcast"),
    path('podcast/', list_podcasts, name="podcast_list"),
    path('podcast/<slug:slug>/', podcast_details, name="podcast_details"),  # ✅ fixed
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
