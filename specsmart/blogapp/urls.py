from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blogapp'

urlpatterns = [
    # path('', views.main_view, name='index'),
    path('', views.MainView.as_view (), name='index'),

    path('contacts/', views.contact_view, name='contacts'),
    path('about/', views.AboutDetailView.as_view (), name='about'),
    path('elements/', views.ElementsView.as_view (), name='elements'),
    path('blogs/', views.BlogsView.as_view (), name='blogs'),
    path('blog/', views.BlogView.as_view (), name='blog'),
    path('post/<int:id>/', views.PostView.as_view (), name='post'),
    # path('post/<int:id>/', views.post, name='post'),
    path('tag-list', views.TagListView.as_view (), name='tag_list'),
    path('tag-detail/<int:pk>/', views.TagDetailView.as_view (), name='tag_detail'),
    path('tag-create/', views.TagCreateView.as_view (), name='tag_create'),
]
