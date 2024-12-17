from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    category = models.CharField(max_length=100, choices=[
        ('1', 'Option 1'), ('2', 'Option 2'), ('3', 'Option 3')
        ])