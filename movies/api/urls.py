from movies.api.views import MovieDetails, MovieSearch, create_review
from django.urls import path

app_name = 'movies_api'

urlpatterns = [
    path('movie/', MovieDetails.as_view(), name='search_movie'),
    path('moviedetails/<title>/', MovieSearch.as_view(), name='moviedetails'),
    path('review/create/', create_review, name='review_create'),
]
