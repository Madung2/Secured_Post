from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from secured_posts.pagination import PaginationHandlerMixin, BasePagination
from .models import Post as PostModel
from .serializers import PostSerializer

from post.services.post_service import get_post, create_post, put_post, delete_post, has_valid_password, has_valid_post_id


class PostView(APIView, PaginationHandlerMixin):
    pagination_class = BasePagination
    def get(self):
        get_serializer = get_post(self)
        if get_serializer:
            return Response(get_serializer, status=status.HTTP_200_OK)
        return Response({"detail" : "정확한 페이지를 입력해주세요"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        create_serializer = create_post(request)
        if create_serializer:
            return Response(create_serializer)

    
    def put(self, request, id):
        if has_valid_post_id:        
            if has_valid_password:
                put_serializer = put_post(request.data, id)
                return Response(put_serializer, status=status.HTTP_200_OK)
            return Response({"detail" : "유효한 비밀번호가 아닙니다."},  status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail" : "게시물이 존재하지 않습니다"},  status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):

        if has_valid_post_id:
            if has_valid_password:
                delete_post(request, id)
                return Response({"detail" : "성공적으로 삭제하셨습니다"}, status=status.HTTP_200_OK)
            return Response({"detail" : "유효한 비밀번호가 아닙니다."},  status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail" : "게시물이 존재하지 않습니다"},  status=status.HTTP_404_NOT_FOUND)
