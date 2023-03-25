from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models import TextChoices

class GradeChoice(TextChoices):
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2
    ONE = 1


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        'feedback_app.Product',
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Продукты'
    )
    text = models.TextField(
        max_length=3000,
        null=False,
        verbose_name='Текст отзыва'
    )
    grade = models.CharField(
        max_length=100,
        null=False,
        verbose_name='Категория',
        choices=GradeChoice.choices,
        default=GradeChoice.ONE
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время обновления')
    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False)
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True,
        default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.text} - {self.grade}"
