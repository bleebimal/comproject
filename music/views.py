from django.http import Http404
#from django.http import HttpResponse
from .models import Album
# from django.template import loader
from django.shortcuts import render

def index(request):

    all_albums = Album.objects.all()
    # template = loader.get_template('music/index.html')

    # return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)

    except Album.DoesNotExist:
        raise Http404("The Page Does not Exist")

    return render(request, 'music/detail.html', {'album': album})
