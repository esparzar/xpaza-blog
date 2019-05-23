from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	#blog properties
		author = models.ForeignKey('auth.User')
		title = models.CharField(max_length=200)
		published_date = models.DateTimeField(blank=True, null=True)
		created_date = models.DateTimeField(default=timezone.now)
		text = models.TextField()

def publish(self):
	self.published_date = timezone.now()
	self.save()

def __str__(self):
	return self.title


