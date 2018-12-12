from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DeleteView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')




















# from django.http import Http404
# #from django.http import HttpResponse
# from .models import Album, Song
# # from django.template import loader
# from django.shortcuts import render, get_object_or_404
#
#
# def index(request):
#
#     all_albums = Album.objects.all()
#     # template = loader.get_template('music/index.html')
#
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'music/index.html', {'all_albums': all_albums})
#
#
# def detail(request, album_id):
#     # try:
#     #     album = Album.objects.get(id=album_id)
#     #
#     # except Album.DoesNotExist:
#     #     raise Http404("The Page Does not Exist")
#
#     album = get_object_or_404(Album, id=album_id)
#
#     return render(request, 'music/detail.html', {'album': album})
#
#
# def favorite(request, album_id):
#     album = get_object_or_404(Album, id=album_id)
#     try:
#         selected_song = album.song_set.get(id=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'error_message': "Nothing is here",
#         })
#     else:
#         if selected_song.is_favorite:
#             selected_song.is_favorite = False
#         else:
#             selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})

