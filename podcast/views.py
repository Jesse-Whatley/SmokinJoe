from django.shortcuts import render

# Create your views here.

def podcast_list_view(request):
    return render(request, 'podcast/podcast_list.html', {
        
    }) 