from django.db import models
from django.conf import settings
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'videos/{filename}'.format(filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, upload_to="photos/")
    is_active = models.BooleanField(default=True)
    birthday = models.DateField(null=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('index')


class Channel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_channel")
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True)
    subscribers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="channel_subscribers",
    )

    def __str__(self):
        return self.title


class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="video_channel", default="Anonymus")
    title = models.CharField(max_length=50)
    image = models.ImageField(_("Image"), upload_to=upload_to, default="videos/default.jpg")
    video = models.FileField(_("Video"), upload_to=upload_to, default="videos/default.png")
    description = models.CharField(max_length=255)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='video_post', null=True, blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='video_post_dislike', null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    def total_likes(self):
        return self.likes.count()

    def total_disikes(self):
        return self.dislikes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s' % (self.video.title, self.user)

    def get_absolute_url(self):
        return reverse('index')


class Email(models.Model):
    client_name=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255, null=True)
    email=models.EmailField(null=True)
    message=models.TextField()

    def __str__(self):
        return self.client_name