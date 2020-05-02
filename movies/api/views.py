from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from movies.models import Movie, Review
from movies.api.serializers import MoviesSerializer, ReviewSerializer, MoviesOverviewSerializer
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from django.db.models import Avg
from rest_framework.decorators import api_view
from django.contrib.auth.models import User 



class MovieDetails(ListAPIView):   
    queryset = Movie.objects.all()
    serializer_class = MoviesSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['title']


class MovieSearch(APIView):

    def get(self, request, title, format=None):
        
        movie_qs = Movie.objects.filter(title=title.capitalize())
        if movie_qs.exists():
            movie = Movie.objects.get(title=title.capitalize())
            review = Review.objects.filter(object_id=movie.id)
            avg_rating =  review.aggregate(Avg('rating'))
            num_of_comments =  review.count()
            serializer = MoviesOverviewSerializer(movie)
            serialized_data = serializer.data
            serialized_data['average_rating'] = round(avg_rating['rating__avg'],1)
            serialized_data['num_of_comments'] = num_of_comments
            return Response(serialized_data)
        else:
            data = {"error": "No movie found"}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)



@api_view(['POST'], )
def create_review(request):
    if request.data.get('user') != None:
        user = User.objects.get(pk=request.data['user'])
        review = Review(user=user)    
        if request.method == "POST":
            serializer = ReviewSerializer(review, data=request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)

            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:        
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'msg': 'User ID Required to create review'})