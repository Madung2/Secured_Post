from rest_framework import serializers
from .models import Post as PostModel
from django.contrib.auth.hashers import make_password

from post.services.post_service import has_numbers

class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['id','title', 'content', 'created_at', 'updated_at']


class PostSerializer(serializers.ModelSerializer):
    
    def validate(self, data):
        password= data['password']
        default_len=6

        if not has_numbers(password): 
            raise serializers.ValidationError(detail={"detail": "비밀번호에 숫자를 포함해주세요"})
        if len(password)<default_len:
            raise serializers.ValidationError(detail={"detail": "비밀번호는 6자리 이상이어야 합니다"})
        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        post=PostModel(**validated_data)
        post.save()
        return validated_data
    
    class Meta:
        model = PostModel
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }
