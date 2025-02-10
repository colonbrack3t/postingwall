from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import *

def index(request):
    return render(request, 'html/index.html', {"siteInfo" : SiteInfo.objects.first() })

def new_post(request):
    return render(request, 'html/submition.html', {"siteInfo" : SiteInfo.objects.first() })

def load_more(request):
    page = int(request.GET.get('page', 1))
    items_per_page = 5

    media_items = MyImageModel.objects.all().filter(publish=True).order_by('-created_at')
    paginator = Paginator(media_items, items_per_page)

    if page > paginator.num_pages:
        return JsonResponse({'media': []})  # No more items

    media_data = []
    for item in paginator.page(page):
        media_data.append({
            'image_url': item.image.url if item.image else None,
            'video_url': item.video.url if item.video else None,
            'text': item.text if item.text else None,
            'created_at' : item.created_at.strftime("%b %d %Y, %I:%M:%S%p"),
            'author' : item.author
        })

    return JsonResponse({'media': media_data})
