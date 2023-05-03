from django.db import models


from clients.models import Client

class Artist(models.Model):
    name = models.CharField(max_length=255)
    works = models.ManyToManyField(Work, related_name='artists')

    def __str__(self):
        return self.name

