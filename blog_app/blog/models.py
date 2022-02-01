from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('blog_list')
