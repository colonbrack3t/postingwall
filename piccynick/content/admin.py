from django.contrib import admin
from .models import MyImageModel

@admin.register(MyImageModel)
class MyImageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'text', 'created_at')
