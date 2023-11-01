from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_year = models.IntegerField()
    photo = models.ImageField(upload_to='movie_photos/')
    plot = models.TextField()
    viewing_date = models.DateField()
    rating = models.FloatField()
