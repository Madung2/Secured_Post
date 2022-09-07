from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from secured_posts.pagination import PaginationHandlerMixin, BasePagination
from .models import Post as PostModel
from .serializers import PostSerializer

from post.services.post_service import get_post, create_post, put_post
# Create your views here.


class PostView(APIView, PaginationHandlerMixin):
    pagination_class = BasePagination
    def get(self, request):
        get_post_serializer = get_post(self)
        return Response(get_post_serializer)

    def post(self, request):
        create_post_serializer = create_post(request)
        return Response(create_post_serializer, status=status.HTTP_200_OK)

    
    def put(self, request, id):
        put_post_serializer = put_post(request, id)
        return Response(put_post_serializer, status=status.HTTP_200_OK)       


    def delete(self, request, pk):
        pass