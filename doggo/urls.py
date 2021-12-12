from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def home(request) :
    return HttpResponse('website coming soon.........')

urlpatterns = [
    path('user/' , include('userManagement.urls')),
    path('admin/', admin.site.urls),
    path('' , home)
]
# urlpatterns = urlpatterns + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
