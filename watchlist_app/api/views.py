# from tempfile import TemporaryFile
from django.shortcuts import render
from rest_framework.views import APIView
from watchlist_app.models import StreamPlatform,WatchList,Review
from watchlist_app.api.serializers import StreamPlatformSerializers,WatchListSerializer,ReviewSerializer
from rest_framework import generics
from watchlist_app.api.permissions import AdminOrReadOnly,IsOwnerOrReadOnly
from rest_framework import viewsets
from django.http import Http404
from rest_framework import mixins
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
# from rest_framework.response import Response
from rest_framework.views import APIView




#Using Generic CLass Based Views

# class StreamPlatformListAV(generics.ListCreateAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializers


# class StreamPlatformDetailsAV(generics.RetrieveUpdateDestroyAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializers


# Using Router and VIewsets

# class StreamPlatformViewset(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing accounts.
#     """
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializers


# Using Mixins

# class StreamPlatformListAV(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializers

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class StreamPlatformDetailsAV(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializers

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#Using Classs Based Views

class StreamPlatformListAV(APIView):
    permission_classes=[AdminOrReadOnly]
    def get(self, request, format=None):
        snippets = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializers(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StreamPlatformSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class StreamPlatformDetailsAV(APIView):

    def get(self, request, pk, format=None):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializers(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_404_NOT_FOUND)
    
        serializer = StreamPlatformSerializers(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

  
    
    
class AddWatchlist(APIView):
    def post(self,request,pk):
        pk=self.kwargs.get('pk')
        movie=StreamPlatform.objects.get(pk=pk)
        print(movie)
        seriailizer=WatchListSerializer(data=request.data)
        if seriailizer.is_valid():
            seriailizer.save(platform=movie)
            return Response(seriailizer.data,status=status.HTTP_201_CREATED)
        return Response(seriailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class AddWatchlist(generics.CreateAPIView):
#     serializer_class=WatchListSerializer
    
#     def perform_create(self, serializer):
#         pk=self.kwargs['pk']
#         movie=StreamPlatform.objects.get(pk=pk)
#         serializer.save(platform=movie)      
    
    
      
class WatchListAV(APIView):

    permission_classes=[IsAuthenticated]
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        movie = WatchList.objects.all()
        serializer = WatchListSerializer(movie, many=True)
        return Response(serializer.data)


    
class WatchListDetailsAV(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, pk, format=None):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def post(self,request, pk,format=None):
        user=self.request.user
        pk=self.kwargs['pk']
        movie=StreamPlatform.objects.get(pk=pk)
        
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(platform=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_404_NOT_FOUND)
    
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewCreate(APIView):
    def post(self, request,pk,format=None):
     
        pk=self.kwargs.get('pk')
        movie=WatchList.objects.get(pk=pk)
        user=self.request.user
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review_queryset=Review.objects.filter(watchlist=movie,review_user=user)
            if review_queryset.exists():
                raise ValidationError('you have already reviewed this moive')  
        
            if movie.number_rating==0:
                movie.avg_rating=serializer.validated_data['rating']
            else:
                movie.avg_rating=(movie.avg_rating +serializer.validated_data['rating'])/2
        
            movie.number_rating=movie.number_rating + 1
            movie.save()
            serializer.save(watchlist=movie,review_user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
class ReviewDetailListAV(APIView):
 
    def get(self, request, pk,format=None):
        pk=self.kwargs.get('pk')
        movie = Review.objects.filter(pk=pk)
        serializer = ReviewSerializer(movie, many=True)
        return Response(serializer.data)
    
class ReviewListAV(APIView):
  
    
    def get(self, request,format=None):
        movie=Review.objects.all()
        serializer = ReviewSerializer(movie, many=True)
        return Response(serializer.data)
    

class ReviewDetailsAV(APIView):
    permission_classes=[IsAdminUser]
    

    def get(self, request,pk ,format=None):
        try:
            movie = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(movie)
        return Response(serializer.data)
    
    def post(self, request,pk, format=None):
        user=self.request.user
        pk=self.kwargs['pk']
        movie=WatchList.objects.get(pk=pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(watchlist=movie,review_user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, pk, format=None):
        try:
            movie = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_404_NOT_FOUND)
    
        serializer = ReviewSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            movie = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'error': 'movie not found'},status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    