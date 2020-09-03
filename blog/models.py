from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Article(models.Model):
    title   = models.CharField(max_length=120)
    content = models.TextField()
    active  = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return f"Article/{self.id}"

    def get_absolute_url(self):
        return reverse('blog:article-details' , kwargs={ "id" :self.id})