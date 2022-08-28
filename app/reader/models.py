from django.db import models

# Create your models here.


class Reader(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()

    def __str__(self):
        return f"Reader with title: {self.title} and content {self.content}"
