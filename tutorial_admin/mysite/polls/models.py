from django.db import models
from django.db.models.deletion import CASCADE

import datetime

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
'''
BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL,
    "question_id" integer NOT NULL
);
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_c5b4b260_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");

COMMIT;
'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # 각 모델에 커스텀 메서드를 추가합니다.
    ## admin에서 객체를 나타내는 설명을 위해 사용됩니다.
    def __str__(self):
        return self.question_text
    ## 데이터가 만들어진 시간을 사용하여 필터링합니다.
    def was_published_recently(self):
        return self.pub_date >= datetime.timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
