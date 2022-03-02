from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User


class StreamPlatform(models.Model):
    name=models.CharField(max_length=255)
    about=models.CharField(max_length=255)
    website=models.URLField(max_length=255)
    
    def __str__(self):
        return self.name
    
class WatchList(models.Model):
    title=models.CharField(max_length=255)
    storyline=models.CharField(max_length=255)
    avg_rating=models.FloatField(default=0)
    number_rating=models.IntegerField(default=0)
    platform=models.ForeignKey(StreamPlatform,related_name='watchlist',on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    description=models.CharField(max_length=255)
    watchlist=models.ForeignKey(WatchList,related_name='review',on_delete=models.CASCADE)

    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating)+"|"+str(self.watchlist.title)