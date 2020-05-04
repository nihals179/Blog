from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    Paragraph = models.TextField()
    author = models.ForeignKey(User,default=None, on_delete=models.SET_DEFAULT)
    def __str__(self):
        return self.title
