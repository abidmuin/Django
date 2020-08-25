from django.http import Http404
from django.shortcuts import render
from .models import Album
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    # * commented out code below is without using templates
    """html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href ="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html) """
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except ObjectDoesNotExist:
        raise Http404("There is no such album!")

    return render(request, 'music/details.html', {'album': album})
