from django.urls import path,include
from . import views
'''
urlpatterns = [
    # path('', views.movielist, name='movielist'),  # For listing all movies
    # path('<pk>/', views.movie_details, name='movie_details'),  # For movie details
    path('', views.MovieListCreate.as_view(), name='movie-list'),  # For listing and creating reviews
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),  # For single review
    # Review-related URLs
 # For listing and creating reviews
    path('reviews/', views.ReviewListCreate.as_view(), name='review-list'),  # For listing and creating reviews
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),  # For single review
]
'''


from rest_framework import routers
from .views import MovieViewSet,ReviewViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register('movies', MovieViewSet, basename='movie')
router.register('reviews', ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]