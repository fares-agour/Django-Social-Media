from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/users/username/filename
    return f'posts/{instance.id}/{filename}'


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts_created", on_delete=models.CASCADE)
    body = models.TextField()
    slug = models.SlugField(max_length=250, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.body

    def save(self, *args, **kwargs):
        self.slug = slugify(self.body)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']


class Friendship(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_friendships")
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_friendships")
    accepted = models.BooleanField(default=False)
