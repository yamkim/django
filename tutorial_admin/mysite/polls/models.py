from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
'''
NOTE
모델 추가 후 할 일
1. settings.py에서 APP을 추가합니다.
2. 모델을 마이그레이션 시킵니다.
   $ python3 manage.py makemigrations polls
3. 모델 변경사항을 데이터 베이스에 적용합니다.
   $ python3 manage.py migrate
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
