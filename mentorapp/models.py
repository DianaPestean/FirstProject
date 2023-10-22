from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserMentor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    gender_choices = (("M", "Male"), ("F","Female"))
    gender = models.CharField(max_length=1, choices=gender_choices)

    def __str__(self):
        return self.first_name


class UserMentee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    gender_choices = (("M", "Male"), ("F","Female"))
    gender = models.CharField(max_length=1, choices=gender_choices)

    def __str__(self):
        return self.first_name
