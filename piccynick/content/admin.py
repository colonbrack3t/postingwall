from django.contrib import admin
from .models import *



@admin.register(MyImageModel)
class MyImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'publish','image', 'text', 'created_at')

@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')