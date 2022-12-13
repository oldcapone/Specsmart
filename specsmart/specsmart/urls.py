from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls', namespace='blog')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('users/', include('usersapp.urls', namespace='users')),

]
# Для того чтобы медия работала на локальном сервере
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)