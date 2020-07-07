from django.shortcuts import render
from .serializers import *
from rest_framework import generics, mixins
from .models import *
from rest_framework.response import Response


class GenresList(generics.ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class GenresDetail(generics.RetrieveAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer


class MoviesList(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    # def perform_create(self, serializer):
    #     # this function is used for authentication
    #     serializer.save(title=self.request.title)

    def post(self, request, *args, **kwargs):
        # self.create is obtained from mixins.createmodelmixin
        return self.create(request, *args, **kwargs)

    # The two functions can be used to update a movie, but it is not needed
    # as we have other function to perform RUD operation
    # def put(self, request, *args, **kwargs):
    #     # self.create is obtained from mixins.createmodelmixin
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     # self.create is obtained from mixins.createmodelmixin
    #     return self.update(request, *args, **kwargs)


class MoviesDetails(generics.RetrieveUpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
# class MoviesUpdateView(generics.UpdateAPIView):
#     queryset = Movies.objects.all()
#     serializer_class = MovieSerializer

    def put(self, request, pk, format=None):
        movie = Movies.objects.get(id=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            print(serializer, "serializer from views.py")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class MoviesDeleteView(generics.DestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
