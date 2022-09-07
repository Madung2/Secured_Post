from logging import raiseExceptions
from django.contrib.auth.hashers import make_password, check_password
from post.serializers import PostSerializer, UpdatePostSerializer
from post.models import Post as PostModel

def has_valid_password(request, id:int)->bool:
    post= PostModel.objects.get(id=id)
    return check_password(request.data['password'],post.password)

def has_valid_post_id(id:int)->bool:
    """
    포스트 아이디값이 유효한지 확인하는 함수
    """
    if PostModel.objects.get(id=id):
        return True
    return False
    
def has_numbers(inputs:str)->bool:
    """
    인자로 받은 문자열에 숫자가 있는지 확인하는 함수
    """
    return any(char.isdigit() for char in inputs)

def get_post(self):
    posts= PostModel.objects.all().order_by('-created_at')
    paged_posts = self.paginate_queryset(posts)
    serializer = PostSerializer(paged_posts, many=True).data
    return serializer

def create_post(request):
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

def put_post(request, id):
    post= PostModel.objects.get(id=id)
    serializer = UpdatePostSerializer(post,data=request, partial=True)     
    serializer.is_valid(raise_exception=True)
    serializer.save()

def delete_post(request, id):
    post= PostModel.objects.get(id=id)
    post.delete()


