from django.db import models
from django.contrib.auth.models import AbstractUser


class UserType(models.Model):
    name = models.CharField(max_length=225)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tipos de usuarios"
        verbose_name = "Tipo de usuario"

class Career(models.Model):
    name = models.CharField(max_length=225)
    code = models.CharField(max_length=4)
    duration = models.IntegerField()
    modality = models.CharField(max_length=225)

class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=225)
    type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    career = models.ManyToManyField(Career, related_name="students", blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"