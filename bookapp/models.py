from django.db import models
from django.contrib.auth.models import User
  # Create your models here.

class book(models.Model):
    book_name=models.CharField(max_length=50)
    descirtion=models.TextField()



