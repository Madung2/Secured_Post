from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from secured_posts.pagination import PaginationHandlerMixin, BasePagination
from .models import Post as PostModel
from .serializers import PostSerializer

# Create your views here.


class PostView(APIView, PaginationHandlerMixin):
    pagination_class = BasePagination
    def get(self, request):
        posts= PostModel.objects.all().order_by('-created_at')
        paged_posts = self.paginate_queryset(posts)
        serializer = PostSerializer(paged_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        post= PostModel.objects.get(id=id)
        serializer = PostSerializer(post,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pass