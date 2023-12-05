from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    actor_name = models.CharField(max_length=100)
    actor_name = models.CharField(max_length=100)
    director_name = models.CharField(max_length=100)
    total_cost = models.CharField(max_length=100)

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_age = models.IntegerField()
    total_people = models.IntegerField()
    number_of_male = models.IntegerField()
    number_of_female = models.IntegerField()
    no_of_children = models.IntegerField()
    required_seats = models.IntegerField()
