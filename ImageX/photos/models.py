
from django.db import models
from django.urls import reverse

class Gallery(models.Model):
    creater = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.title

class Photographer(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return "Photographer is" + self.name

class Tag(models.Model):
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return "#" + self.text
    
class Category(models.Model):
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.text

class Picture(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    file = models.FileField()
    uploader_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('photos:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.title + '-' + self.description