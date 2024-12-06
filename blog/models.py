from django.db import models
from course.models import Register

class Blog(models.Model):
    image = models.ImageField(upload_to='blog_image/')
    title = models.CharField(max_length=150)
    author_name = models.ForeignKey(Register, on_delete=models.CASCADE)
    category = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
