from django.db.models import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView, status

from movies.serializers import MovieSerializer

from .models import Movie


class MovieList(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MovieDetail(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk=pk)

        movie.delete()
        return Response(
            {"message": f"deleted successfully!"},
            status=status.HTTP_204_NO_CONTENT,
        )

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)

        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(movie, request.data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
