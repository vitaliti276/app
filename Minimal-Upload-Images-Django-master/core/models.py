from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.TextField()
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title