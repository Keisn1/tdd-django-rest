from django.urls import path

from .views import MovieDetail, MovieList

# router = routers.DefaultRouter()
# router.register(r"model-viewset", MovieViewSet)
# urlpatterns = ["", include(router.urls)]

urlpatterns = [
    path("movies/", MovieList.as_view()),
    path("movies/<int:pk>/", MovieDetail.as_view()),
]
