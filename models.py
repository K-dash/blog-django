from msilib.schema import Class
from turtle import title
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
