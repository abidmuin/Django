from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# ? Creating custom manager to retrieve data from database


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
            .filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }
    title = models.CharField(max_length=250)
    # ? slug => https://stackoverflow.com/a/427160/8525893
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    # ? auto_now_add, the date will be saved automatically when creating an object.
    created = models.DateTimeField(auto_now_add=True)
    # ? auto_now, date will be updated automatically when saving an object
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    # ? Custom manager for db query
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom

    class Meta:
        # ?sort results by the publish field in descending order by default
        # ? negative prefix (-) means descending order when query is made in database
        # ? Thus, recent posts appear first.
        ordering = ('-publish',)

    # ? __str__() method is default human-readable representation of the object
    def __str__(self):
        return self.title

    # ? Canonical URLs
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
