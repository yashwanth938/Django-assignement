from django.db import models
from django.contrib.auth.models import User
from artists.models import Work

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work, related_name='clients')

    def __str__(self):
        return self.name
