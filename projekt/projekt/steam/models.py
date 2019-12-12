import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ModelForm

class Developer(models.Model):
    name = models.CharField(max_length=50)
    logo = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    category = models.ManyToManyField(Category)

    #return "%s %s" % (self.first_name, self.last_name)
    def __str__(self):
        return self.name

class Review(models.Model):
    author_name = models.CharField(max_length=50)
    text = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    stars = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    likes = models.IntegerField(default=0)

    def __str__(self):
        s = self.author_name + "; " + self.text
        return s

class Choice(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
