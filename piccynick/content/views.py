from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import MyImageModel

def index(request):
    return render(request, 'html/index.html')

def load_more(request):
    page = int(request.GET.get('page', 1))
    items_per_page = 2

    media_items = MyImageModel.objects.all().order_by('-id')
    paginator = Paginator(media_items, items_per_page)

    if page > paginator.num_pages:
        return JsonResponse({'media': []})  # No more items

    media_data = []
    for item in paginator.page(page):
        media_data.append({
            'image_url': item.image.url if item.image else None,
            'video_url': item.video.url if item.video else None,
            'text': item.text if item.text else None,
            'created_at' : item.created_at
        })

    return JsonResponse({'media': media_data})
