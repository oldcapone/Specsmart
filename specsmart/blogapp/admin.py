from django.contrib import admin
from django import forms
from django.contrib import admin
from .models import Category, Post, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label="Краткое описание", widget=CKEditorUploadingWidget())
    description_detail = forms.CharField(label="Детальное описание", widget=CKEditorUploadingWidget())
    price = forms.IntegerField(label="Цена")
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)