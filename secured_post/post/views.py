from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from secured_posts.pagination import PaginationHandlerMixin, BasePagination
from .models import Post as PostModel
from .serializers import PostSerializer

# Create your views here.


class PostView(APIView, PaginationHandlerMixin):
    def get(self, request):
        posts= PostModel.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        pass
    def delete(self, request, pk):
        pass