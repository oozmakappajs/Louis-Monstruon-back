from django.db import models

class Dress(models.Model):
    marca = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True) 
    edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.marca