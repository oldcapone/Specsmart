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

def clear_price(modeladmin, request, queryset):
    queryset.update(price='0')
clear_price.short_description = "Сбросить цены"

def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
set_active.short_description = "Активировать"

def set_deactive(modeladmin, request, queryset):
    queryset.update(is_active=False)
set_deactive.short_description = "Дективировать"

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['name', 'category', 'display_tags', 'price', 'create', 'rating', 'is_active']
    actions = [clear_price, set_active, set_deactive]

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    actions = [set_active, set_deactive]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag, TagAdmin)