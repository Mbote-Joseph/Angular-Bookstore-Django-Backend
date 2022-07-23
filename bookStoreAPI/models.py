from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(auto_now_add=True)
    pages= models.IntegerField(default=0)
    # category = models.CharField(max_length=255)
    # in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publisher = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title