from django.contrib.auth.hashers import make_password, check_password
from post.serializers import PostSerializer, UpdatePostSerializer
from post.models import Post as PostModel


def get_post(self):
    posts= PostModel.objects.all().order_by('-created_at')
    paged_posts = self.paginate_queryset(posts)
    serializer = PostSerializer(paged_posts, many=True).data
    return serializer

def create_post(request):
    request.data['password'] = make_password(request.data['password'])
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return serializer.errors

def put_post(request, id):
    post= PostModel.objects.get(id=id)

    if check_password(request.data['password'],post.password):
        serializer = UpdatePostSerializer(post,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        return serializer.errors
    return "통과 안했습니다"
    # return serializer.errors
