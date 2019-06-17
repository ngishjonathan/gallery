from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
   return render(request,'welcome.html')
   
def search_results(request):

    if 'image' in request.GET and request.GET["search_item"]:
        search_term = request.GET.get("search_item")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
