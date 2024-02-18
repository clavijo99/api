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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Carreras"
        verbose_name = "Carrera"

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

class Modality(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Modalidades"
        verbose_name = "Modalidad"

class Lounge(models.Model):
    name = models.CharField(max_length=225)
    capacity = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Salones"
        verbose_name = "Salon"

class Semester(models.Model):
    career_id = models.CharField(max_length=50)
    day = models.CharField(max_length=20)
    credits = models.IntegerField()

    def __str__(self):
        return self.day
    
    class Meta:
        verbose_name_plural = "Semestre"
        verbose_name = "Semestre"

class Matter(models.Model):
    name = models.CharField(max_length=50)
    career_id = models.ForeignKey(Career, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    credits = models.IntegerField()
    modality_id = models.ForeignKey(Modality, on_delete=models.CASCADE)
    lounge_id = models.ForeignKey(Lounge, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Materias"
        verbose_name = "Materia"