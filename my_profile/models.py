from django.db import models

# Create your models here.
class MyProfile(models.Model):
	user_id = models.CharField(max_length=15)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	aggregate_hotness = models.FloatField()

class Photo(models.Model):
	photo_id = models.CharField(max_length=15)
	user = models.ForeignKey(MyProfile)
	hotness = models.IntegerField(default=0)