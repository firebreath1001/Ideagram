from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=100)
    idea = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)