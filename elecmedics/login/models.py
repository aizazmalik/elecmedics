from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    def __str__(self):
        return self.email