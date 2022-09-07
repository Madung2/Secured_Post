from rest_framework import serializers
from .models import Post as PostModel


def has_numbers(inputs):
    """문자열에 숫자가 있는지 여부 체크

    Args:
        inputs (_type_): _description_

    Returns:
        _type_: bool
    """        
    return any(char.isdigit() for char in inputs)


class PostSerializer(serializers.ModelSerializer):

    
    def validate(self, data):
        password= data['password']
        default_len=6


        if not has_numbers(password): #비밀번호에 숫자가 없는 경우
            raise serializers.ValidationError(detail={"detail": "비밀번호에 숫자를 포함해주세요"})
        if len(password)<default_len:
            raise serializers.ValidationError(detail={"detail": "비밀번호는 6자리 이상이어야 합니다"})
        return data
    
    # def update(self, instance, validated_data):
    #     instance.save()
    #     return instance
    
    class Meta:
        model = PostModel
        fields = '__all__'

        extra_kwargs = {
            'password': {'write_only': True}
        }
