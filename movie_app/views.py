from .models import Movie
from .serializers import MovieSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Review
from .serializers import ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
# Create your views here.


# @api_view(['GET', 'POST'])
# def movielist(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
# class MovieListCreate(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer

# class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
    
    

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def movie_details(request,pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)
    
#     elif request.method == 'PATCH':
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=204)
#     return Response(status=405)



# Review API
# from .models import Review
# from .serializers import ReviewSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import generics


# class ReviewListCreate(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get_serializer_context(self):
#         # Pass the request context to the serializer
#         context = super().get_serializer_context()
#         context['request'] = self.request  # Add the request to the context
#         return context
    

# class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
from .permissions import IsReviewerOrReadOnly
from .filters import MovieFilter
from rest_framework.filters import SearchFilter, OrderingFilter 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related('movie_reviews').all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] 
    filterset_class = MovieFilter
    search_fields = ['name','active']
    ordering_fields = ['name','active']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
 # Ensure the user is authenticated to access this view
    
    
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related('movie').all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewerOrReadOnly,IsAuthenticated]  # Ensure the user is authenticated to access this view

    