from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Record(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Содержание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Название", **NULLABLE)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ['-created_at']  # сортировка записей по дате создания в обратном порядке

    def __str__(self):
        return self.name
