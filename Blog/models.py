from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True )
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(blank=False , upload_to='assets')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE ,blank=True )

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:80] + '...'