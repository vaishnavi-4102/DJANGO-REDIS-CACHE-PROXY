from django.db import models

# Create your models here.
class CachedData(models.Model):
    key = models.CharField(max_length = 250, unique = True)
    value = models.TextField()