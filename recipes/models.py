from django.db import models


class Recipe (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    imagen = models.ImageField(upload_to="cocktails/", null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
