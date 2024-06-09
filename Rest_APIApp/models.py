from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    descriptions = models.TextField()
    price=models.DecimalField( max_digits=5, decimal_places=2)
    stock= models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.name
    