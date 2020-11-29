from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from profiles.models import UserProfile

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    title = models.CharField(max_length=120, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=False)
    slug = models.SlugField(unique=True, max_length=250, default=None)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    status = models.IntegerField(choices=STATUS, null=True, default=0)


    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while BlogPost.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
