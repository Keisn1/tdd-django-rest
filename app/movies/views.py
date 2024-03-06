from django.db.models import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.serializers import MovieSerializer

from .models import Movie


class MovieList(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("hello")
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class MovieDetail(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("Hello")
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


# def movies(request):
#     data = JSONParser().parse(request)
#     serializer = MovieSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data, status=201)
