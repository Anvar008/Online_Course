from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=130)

    def __str__(self):
        return self.title


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.ForeignKey(Register, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='course_image/')
    price = models.CharField(max_length=50)
    views = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Event(models.Model):
    image = models.ImageField(upload_to='events_images/')
    post_add_time = models.DateTimeField()
    title = models.CharField(max_length=150)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title


