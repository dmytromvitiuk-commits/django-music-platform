from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва жанру")
    description = models.TextField(blank=True, verbose_name="Опис жанру")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва треку")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Жанр")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна (якщо платний)")
    is_available = models.BooleanField(default=True, verbose_name="Доступний для прослуховування")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я/Назва виконавця")
    bio = models.TextField(blank=True, verbose_name="Біографія")
    country = models.CharField(max_length=100, verbose_name="Країна")

    def __str__(self):
        return self.name