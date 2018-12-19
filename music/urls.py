from django.conf.urls import url
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^logout/$', views.logout_view, name='logout'),

    #/music/<album_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

#     #/music/<album_id>/favorite
#     url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

    #music/albums/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # music/albums/2/
    url(r'album/(?P<pk>[0-9])/$', views.AlbumUpdate.as_view(), name='album-update'),

    # music/album/2/delete
    url(r'album/(?P<pk>[0-9])/delete/$', views.AlbumDelete.as_view(), name='album-delete')
]

# people that are requesting ep41. I've figured it out my self
# DO THE FOLLOWING:
#
# - In website/urls.py:
# from django.conf.urls import url
# from django.contrib import admin
# from rest_framework.urlpatterns import format_suffix_patterns
# from companies import views
#
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^stocks/', views.StockList.as_view()),
#     url(r'^stocks/(?P<pk>[0-9]+)/', views.StockDetail.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
#
# - In companies/views.py:
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Stock
# from .serializers import StockSerializer
# from django.http import Http404
#
#
# # Lists all stocks or creates a new one
# # stocks/
# class StockList(APIView):
#
#     def get(self, request):
#         stocks = Stock.objects.all()
#         serializer = StockSerializer(stocks, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StockSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class StockDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Stock.objects.get(pk=pk)
#         except Stock.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = StockSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = StockSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
