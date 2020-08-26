from django.shortcuts import render, get_object_or_404
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

    album = get_object_or_404(Album, pk=album_id)

    """[Checks for requested object. If not found then theows an error]

    Raises:
        Http404: [description]

    Returns:
        [type]: [description]
    try:
        album = Album.objects.get(pk=album_id)
    except ObjectDoesNotExist:
        raise Http404("There is no such album!")
    """

    return render(request, 'music/details.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {
            'album': album,
            'error_message': "You didn't select a valid song.",
        })
    finally:
        # ? make Favorite / Unfavorite
        selected_song.is_favorite = not selected_song.is_favorite
        selected_song.save()

        return render(request, 'music/details.html', {'album': album})
