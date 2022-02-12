from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    date_created = models.DateField(auto_now=True)
    date_modified = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='video')

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    date_created = models.DateField(auto_now=True)
    date_modified = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='music')

    def __str__(self):
        return self.name