from django.db import models

# Create your models here.

class Idea(models.Model):
    title = models.CharField(max_length=100)
    idea = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__():
        return str(self.title)
