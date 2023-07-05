from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150, blank=False, null= False)
    description = models.TextField(default='')
    price = models.FloatField(default=0, blank=False)
    image = models.ImageField()
    
    def __str__(self):
        return self.title

