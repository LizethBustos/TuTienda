from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Type(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)
    descripcion = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class ElementImages(models.Model):
    element = models.ForeignKey(Element,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    cover = models.ImageField(Upload_to='images/')


    def __str__(self):
        return self.tittle