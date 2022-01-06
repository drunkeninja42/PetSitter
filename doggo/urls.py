from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.shortcuts import render

def home(request) :
    return render(request, 'index.html')

urlpatterns = [
    path('' , include('userManagement.urls')),
    path('admin/', admin.site.urls),
]
# urlpatterns = urlpatterns + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
