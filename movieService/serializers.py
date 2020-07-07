from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ["pk", "name"]


class MovieSerializer(serializers.ModelSerializer):
    # genreName is a property that was declared in models.
    genreName = serializers.ReadOnlyField()

    class Meta:
        model = Movies
        fields = "__all__"
