from post.serializers import PostSerializer
from post.models import Post as PostModel



def get_post(self):
    posts= PostModel.objects.all().order_by('-created_at')
    paged_posts = self.paginate_queryset(posts)
    serializer = PostSerializer(paged_posts, many=True).data
    return serializer

def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return serializer.errors

def put_post(request, id):
    post= PostModel.objects.get(id=id)
    serializer = PostSerializer(post,data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    return serializer.errors
