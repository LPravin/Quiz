from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    School = 1
    Student = 2

    ROLE_CHOICES = (
        (School, 'School'),
        (Student, 'Student')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


class Quiz(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    quiz_ref = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_reference')
    num = models.SmallIntegerField()
    question = models.CharField(max_length=300)
    option_1 = models.CharField(max_length=50)
    option_2 = models.CharField(max_length=50)
    option_3 = models.CharField(max_length=50)
    option_4 = models.CharField(max_length=50)
    is_multiple_correct = models.BooleanField(default=False)
    is_ans_option_1 = models.BooleanField(default=False)
    is_ans_option_2 = models.BooleanField(default=False)
    is_ans_option_3 = models.BooleanField(default=False)
    is_ans_option_4 = models.BooleanField(default=False)
    description = models.CharField(max_length=200)


class AnswerEntries(models.Model):
    ques_ref = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='ques_reference')
    user_ref = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_reference')
    whether_answered_right = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Answer Entries'
