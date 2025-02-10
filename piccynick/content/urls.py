
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns = [
    path('', views.index, name = "main_page_view"),
    path('new_post', views.new_post, name = "new_post"),
    path('load-more/', views.load_more, name= 'load-more')
] 
