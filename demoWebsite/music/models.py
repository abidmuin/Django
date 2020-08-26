from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(("Artist"), max_length=50)
    album_title = models.CharField(("Album"), max_length=50)
    genre = models.CharField(("Genre"), max_length=50)
    album_logo = models.CharField(("Album logo"), max_length=50)

    def __str__(self):
        return self.album_title + " - " + self.artist


class Song(models.Model):
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    file_type = models.CharField(("File type"), max_length=10)
    song_title = models.CharField(("Song title"), max_length=50)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
