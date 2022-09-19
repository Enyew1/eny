from ast import Return
from distutils.command.upload import upload
from email.mime import image
from os import link
from pyexpat import model

from django.db import models

# HomeSection.
class Home(models.Model):
    name=models.CharField(max_length=20)
    greetings_1=models.CharField(max_length=5)
    greetings_2=models.CharField(max_length=5)
    picture=models.ImageField(upload_to='picture/')
#update time
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
     return self.name
    #About-section
class About(models.Model):
  heading=models.CharField(max_length=50)
  career=models.CharField(max_length=20)
  description=models.TextField(blank=False)
  profile_img=models.ImageField(upload_to='profile/')
  updated=models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.career

#profile section
class Profile(models.Model):
    about=models.ForeignKey(About,on_delete=models.CASCADE)
    social_name=models.CharField(max_length=10)
    link=models.URLField(max_length=200)
#skills section
class Category(models.Model):
  name = models.CharField(max_length=20)
  updated = models.DateTimeField(auto_now=True)
  class Meta:
      verbose_name='skill'
      verbose_name_plural='skills'
  def __str__(self): 
     return self.name
class Skills(models.Model):
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  skill_name=models.CharField(max_length=20)
#Portfolio section
class Portfolio(models.Model):
    image=models.ImageField(upload_to='portfolio/')
    link=models.URLField(max_length=200)
    def __str__(self):
     return f'portfolio{self.id}'