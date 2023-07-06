from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    createdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_blog', kwargs={'pk': self.pk})
