from django.db import models

# Create your models here.

class Encourage(models.Model):
	title = models.CharField(max_length=100)
