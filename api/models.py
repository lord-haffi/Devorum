from django.conf import settings
from django.db import models

# Create your models here.


class Thread(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=65535)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    text = models.TextField(max_length=65535)
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.text > 60:
            return self.id + ": " + self.text[:60] + "..."
        else:
            return self.id + ": " + self.text

