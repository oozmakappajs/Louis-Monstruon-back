from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True) 
    edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name