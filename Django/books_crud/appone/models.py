from pickle import TRUE
from django.db import models
# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    book_price = models.CharField(max_length=255)
    
    


