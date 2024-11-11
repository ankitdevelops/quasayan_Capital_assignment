from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=500)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    text = models.CharField(max_length=200)
    score = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.question.answers.count() >= 4:
            raise ValueError("A question can have at most 4 answers.")
        return super().save()

    def __str__(self):
        return f"{self.question.text} - {self.text}"


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "question"]


class CreditScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    calculated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
