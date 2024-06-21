from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Portifolio(models.Model):
    name = models.CharField(max_length=30)
    client = models.CharField(max_length=30)
    date = models.DateField()
    url = models.URLField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to='media')
    picture2 = models.ImageField(upload_to='media',null=True,blank=True)
    picture3 = models.ImageField(upload_to='media',null=True,blank=True)
    text = models.TextField()
    authter = models.CharField(max_length=30,null=True,blank=True)
    created_at = models.DateTimeField(auto_now = True)

class Service(models.Model):
    picture = models.ImageField(upload_to='media')
    name = models.CharField(max_length=30)
    information = models.CharField(max_length=30)

class Team(models.Model):
    picture = models.ImageField(upload_to='media')
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    information = models.CharField(max_length=30)
    url1 = models.CharField(max_length=30)
    url2 = models.CharField(max_length=30)
    url3 = models.CharField(max_length=30)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=300)

