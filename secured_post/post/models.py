from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField("제목",max_length=20)
    content = models.CharField("내용", max_length=200)
    password = models.CharField("포스트 비밀번호",max_length=128)
    created_at = models.DateTimeField("생성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("마지막 수정 시간", auto_now=True)
