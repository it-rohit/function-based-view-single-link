
from django.urls import path,include
from . views import movie_list,movie_details,create_movies,movie_update,movie_delete

urlpatterns = [
    path('list/',movie_list, name='movie_list'),
    path('<int:pk>/',movie_details, name='movie_details'),
    path('create/', create_movies, name='create_movie'),
    path('update/<int:pk>/', movie_update, name='movie_update'),
    path('delete/<int:pk>/', movie_delete, name='movie_delete'),
]
