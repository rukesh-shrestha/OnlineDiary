from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from ckeditor.fields import RichTextField

# Create your models here.
class Dairy(models.Model):
    title = models.CharField(max_length=200,blank=False)
    body = RichTextField(blank=False,null=True)
    # body = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)


    def __str__(self):
        return self.title
       

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])