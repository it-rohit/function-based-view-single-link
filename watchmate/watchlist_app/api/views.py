from ..models import Movie
from .serializer import MovieSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

# create new movie
@api_view(['POST'])
def create_movies(request):
    if request.method == 'POST':
        data1 = request.data
        serializer1 = MovieSerializer(data = data1)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data)
        else:
            return Response(serializer1.errors)





## all list of movie
@api_view(['GET'])
def movie_list(request):
    movie= Movie.objects.all()
    print("hai")
    serializer1 = MovieSerializer(movie, many=True)
    print("hai")
    return Response(serializer1.data)



## single movie detail
@api_view(['GET'])
def movie_details(request,pk):
    movie= Movie.objects.get(pk=pk)
    serializer1 = MovieSerializer(movie)
    return Response(serializer1.data)

# #update single movie 
@api_view(['PUT'])
def movie_update(request,pk):
    if request.method == 'PUT':
        try:
            movie= Movie.objects.get(pk=pk)
            data1=request.data
            serializer1 = MovieSerializer(instance=movie, data=data1)
            if serializer1.is_valid():
                serializer1.save()
                return Response(serializer1.data)
            else:
                return Response(serializer1.errors)
        except Movie.DoesNotExist:
            return Response({"error": "Movie does not exist"}, status=404)

# #delete  ingle movie using pk
@api_view(['DELETE'])
def movie_delete(request,pk):
    
    if request.method == 'DELETE':
        try:
            movie= Movie.objects.get(pk=pk)
            movie.delete()
            return Response({"message": "Movie deleted successfully"})
        
        except Movie.DoesNotExist:
            return Response({"error": "Movie does not exist"}, status=404)
    # else:
    #     return Response({"error": "Method not allowed"}, status=405)
    

