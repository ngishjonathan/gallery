from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def index(request):
    image_catalogue = Image.all_images()
    location = Location.get_location()
    return render(request,'all-photos/index.html',{"all_images":image_catalogue,"locations":location})

def search_images(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        search_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request,'all-photos/search.html',{"message":message,"images_searched":search_images})

    else:
        message = "You haven't searched yet"
        return render(request,"all-photos/search.html",{"message":message})

def filter_location(request,image_id):
    try:
        location = Location.get_location()
        located_images = Image.objects.filter(image_location=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'all-photos/image.html',{"located_images":located_images,"locations":location})
