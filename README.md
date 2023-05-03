# Django-assignement

To create the backend structure with the specified requirements, we will need to use Django, which is a powerful web framework for Python. We will follow the Model-View-Template (MVT) architecture of Django. The MVT architecture separates the application into three main components:

Models - This is the database layer of the application where we define the structure of the data.

Views - This is the logic layer of the application where we define how the data is processed and presented.

Templates - This is the presentation layer of the application where we define how the data is displayed to the user.


Create the Client model
Next, we need to create the Client model which contains the name and user instance (Foreign Key). We will define this model in the models.py file of the app we are going to create. To create the app, we will run the following command:



##In the models.py file, we will define the Client model 


    from django.db import models
    from django.contrib.auth.models import User

    class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

#Here, we have defined a Client model with two fields: name and user. The name field is a CharField that stores the name of the client, and the user field is a ForeignKey to the built-in User model of Django. The on_delete=models.CASCADE argument ensures that if the user is deleted, all associated clients will be deleted as well.

 #Create the Artist and Work models
Next, we need to create the Artist and Work models. We will define these models in the models.py file of the app we are going to create. To create the app, we will run the following command:

#new directory named artists


In the models.py file, we will define the Artist and Work models 



    from django.db import models
    
    from django.db import models

    class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#In client

    class Work(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    work_type = models.CharField(max_length=255)
    link = models.URLField()
    
    def __str__(self):
        return f"{self.artist.name}'s {self.work_type} work"

Here, we have defined an Artist model with a name field that stores the name of the artist. We have also defined a Work model with three fields: artist (a ForeignKey to the Artist model), work_type (a CharField that stores the type of work, e.g. "YouTube" or "Instagram"), and link (a URLField that stores the link to the work). The __str__ method of the Work model returns a string representation of the work that includes the artist's name and the type of work.

# Create the ManyToManyField
Since we need to link the Client and Work models with a many-to-many relationship, we will add a works field to the Client model, which is a ManyToManyField that relates to the Work model. We will also add a clients field to the Work model, which is a ManyToManyField that relates to the Client model. To do this, we will modify the models.py file of the clients and artists apps 





    from django.db import models
    from django.contrib.auth.models import User
    from artists.models import Work

    class Client(models.Model):
        name = models.CharField(max_length=255)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        works = models.ManyToManyField(Work, related_name='clients')

    def __str__(self):
        return self.name




    from django.db import models
    from clients.models import Client

    class Artist(models.Model):
        name = models.CharField(max_length=255)
        works = models.ManyToManyField(Work, related_name='artists')

    def __str__(self):
        return self.name



Here, we have added a works field to the Client model and a clients field to the Work model, both of which are ManyToManyField fields. The related_name argument allows us to use reverse relationships to access the related objects.



#Create the API endpoints
Next, we need to create the API endpoints to show works, integrate filtering with work type, and integrate search with artist name. We will use Django Rest Framework (DRF) to create the API endpoints. To install DRF, you can run the following command:

##pip install djangorestframework


#After installing DRF, we need to create serializers and views for the Work and Artist models. We will define these in the serializers.py and views.py files of the artists app.


    from rest_framework import serializers
    from artists.models import Work, Artist

    class WorkSerializer(serializers.ModelSerializer):
        artist = serializers.ReadOnlyField(source='artist.name')

    class Meta:
        model = Work
        fields = ('id', 'artist', 'work_type', 'link')

    class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'works')





    from rest_framework import generics, filters
    from artists.models import Artist, Work
    from artists.serializers import ArtistSerializer, WorkSerializer

    class WorkList(generics.ListAPIView):
        queryset = Work.objects.all()
        serializer_class = WorkSerializer
        filter_backends = [filters.SearchFilter, filters.OrderingFilter]
        search_fields = ['artist__name']
        ordering_fields = ['artist__name', 'work_type']

    class ArtistList(generics.ListAPIView):
        queryset = Artist.objects.all()
        serializer_class = ArtistSerializer






Here, we have defined a WorkSerializer and an ArtistSerializer that serialize the Work and Artist models, respectively. We have also defined a WorkList and an ArtistList view that retrieve all works and artists, respectively, and serialize them using the appropriate serializer. The WorkList view also includes filtering and ordering capabilities using DRF's built-in SearchFilter and OrderingFilter.
