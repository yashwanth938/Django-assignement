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
