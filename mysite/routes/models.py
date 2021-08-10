from django.db import models

# Create your models here.
bacon_id = 4724

class Person(models.Model):
    name = models.IntegerField()

class Movie(models.Model):
    title = models.IntegerField()

class Step(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    next_step = models.ForeignKey(Person, on_delete=models.CASCADE,related_name='next_step_person',default=bacon_id)
