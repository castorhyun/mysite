# Create your models here.
# 객체 생성하는 파일 models.py

from django.db import models
from django.utils import timezone

# class 객체정의
# Post : 객체명 (object)
# models : Post 가 장고모델이며 데이터베이스에 저장될 객체라는 것을 전달해줌
# 아래 변수들은 객체의 속성들
class Post(models.Model):
    author = models.ForeignKey('auth.User') # ForeignKey : 다른 모델에 대한 링크
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publised_date = models.DateTimeField(blank=True, null=True)

    # def 함수/메서드 정의
    def publish(self):
        self.publised_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

