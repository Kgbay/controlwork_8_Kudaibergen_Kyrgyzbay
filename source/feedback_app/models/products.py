from django.db import models
from django.utils import timezone
from django.db.models import TextChoices


class CategoryChoice(TextChoices):
    GAMES = ('Games', 'Игры')
    HEALTH = ('Health', 'Здоровье')
    SPORT = ('Sport', 'Спорт')
    BEAUTY = ('Beauty', 'Красота')
    KITCHEN = ('Kitchen', 'Кухня')
    CHOTHES = ('Clothes', 'Одежда')
    OTHER = ('Other', 'Разное')


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Наименование')
    category = models.CharField(
        max_length=100,
        null=False,
        verbose_name='Категория',
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER)
    description = models.TextField(
        max_length=3000,
        null=True,
        verbose_name='Описание',
        default='Описание товара')
    image = models.ImageField(
        null=False,
        upload_to='user_picture',
        verbose_name='Изображения'
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
        return f"{self.name} - {self.category}"

