from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    actor_name = models.CharField(max_length=100)
    actor_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    total_cost = models.CharField(max_length=100)