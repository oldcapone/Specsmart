from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('contacts/', views.contact_form, name='contacts'),
    path('about/', views.about, name='about'),
    path('elements/', views.elements, name='elements'),
    path('blogs/', views.blog, name='blogs'),
    path('blog/', views.elements, name='blog'),
    path('post/<int:id>/', views.post, name='post'),
]
