from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models import IntegerChoices

from feedback_app.models import Product


class GradeChoice(IntegerChoices):
    FIVE = (5, 'Отлично')
    FOUR = (4, 'Хорошо')
    THREE = (3, 'Среднее')
    TWO = (2, 'Плохо')
    ONE = (1, 'Очень Плохо')


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукты'
    )
    text = models.TextField(
        max_length=3000,
        null=False,
        verbose_name='Текст отзыва'
    )
    grade = models.IntegerField(
        null=False,
        verbose_name='Оценка',
        choices=GradeChoice.choices,
        default=GradeChoice.THREE
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
