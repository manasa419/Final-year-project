from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static #this is needed for file and image upload
from django.conf import settings
from hrms import views

import hrms

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hrms.urls', namespace = 'hrms')),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
